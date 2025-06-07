from cai.cli import run_cai_cli, update_agent_models_recursively
from cai.util import fix_litellm_transcription_annotations
from cai.agents import get_agent_by_name
import os

class CAISlackAgentRunner:
    def __init__(self, session):
        self.session = session

    def run_loop(self):
        if not fix_litellm_transcription_annotations():
            print("[CAI] Failed LiteLLM patch")

        agent_type = os.getenv('CAI_AGENT_TYPE', "one_tool_agent")
        model_name = os.getenv('CAI_MODEL', "alias0")
        agent = get_agent_by_name(agent_type)

        if hasattr(agent, 'model'):
            agent.model.disable_rich_streaming = True
            agent.model.suppress_final_output = False

        update_agent_models_recursively(agent, model_name)

        run_cai_cli(agent, input_control=self.session.get_user_message)