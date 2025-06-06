import os
from queue import Queue, Empty
from slack_sdk import WebClient
from interface.slack.cai_slack_interface import interface

from cai.cli import run_cai_cli, update_agent_models_recursively
from cai.util import fix_litellm_transcription_annotations, color
from cai.agents import get_agent_by_name


# From your Slack event (e.g., `message` event):
interface.receive_message("agent, what can you do?")

"""Run the CAI agent CLI loop in a thread."""
try:
    # Patch LiteLLM if needed
    if not fix_litellm_transcription_annotations():
        print(color("Failed LiteLLM patch", color="red"))

    agent_type = os.getenv('CAI_AGENT_TYPE', "one_tool_agent")
    model_name = os.getenv('CAI_MODEL', "alias0")

    agent = get_agent_by_name(agent_type)

    if hasattr(agent, 'model'):
        if hasattr(agent.model, 'disable_rich_streaming'):
            agent.model.disable_rich_streaming = True
        if hasattr(agent.model, 'suppress_final_output'):
            agent.model.suppress_final_output = False

    update_agent_models_recursively(agent, model_name)

    try:
        run_cai_cli(agent, input_control=interface.get_user_message)
    except Exception as e:
        print(f"[Agent Thread Error] {e}")
    finally:
        running = False

except KeyboardInterrupt as e:
    print(f"[AgentLoop] Interrupted: {e}")
except Exception as e:
    print(f"[AgentLoop] Exception occurred: {e}")