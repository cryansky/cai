"""
First prototype of a reasoner agent

using reasoner as a tool call

support meta agent may better @cai.agents.meta.reasoner_support
"""
from cai.tools.misc.reasoning import think
from cai.types import Agent  # pylint: disable=import-error
from cai.util import load_prompt_template  # Add this import
import os

ssdlc_thought_agent_system_prompt = load_prompt_template("prompts/system_ssdlc_thought_router.md")

# Thought Process Agent for analysis and planning
ssdlc_thought_agent = Agent(
    name="ThoughAgent",
    model=os.getenv('CAI_MODEL', "qwen2.5:14b"),
    description="""Agent focused on analyzing and planning the next steps
                   in SSDLC workflow.""",
    instructions=ssdlc_thought_agent_system_prompt,
    functions=[think],
    parallel_tool_calls=False
)
