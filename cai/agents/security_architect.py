"""Security Architect Base Agent"""
import os
from cai.types import Agent  # pylint: disable=import-error
from cai.util import load_prompt_template  # Add this import

from cai.tools.reconnaissance.generic_linux_command import (  # pylint: disable=import-error # noqa: E501
    generic_linux_command
)

from cai.tools.reconnaissance.exec_code import (  # pylint: disable=import-error # noqa: E501
    execute_code
)

from cai.tools.web.search_web import (  # pylint: disable=import-error # noqa: E501
    make_web_search_with_explanation,
)

from cai.tools.reconnaissance.document import (  # pylint: disable=import-error # noqa: E501
    extract_pdf_content,
    add_comment_to_pdf
)

# Prompts
security_architect_agent_system_prompt = load_prompt_template("prompts/system_security_architect_agent.md")

# Define functions list based on available API keys
functions = [
    generic_linux_command,
    execute_code,
    extract_pdf_content,
    add_comment_to_pdf,
]

if os.getenv('PERPLEXITY_API_KEY'):
    functions.append(make_web_search_with_explanation)

security_architect_agent = Agent(
    name="Security Architect Agent",
    instructions=security_architect_agent_system_prompt,
    description="""Agent that specializes in gathering knowledge from design review documents.
                   Expert in identifying potential vulnerability and security risk based on design documents.""",
    model=os.getenv('CAI_MODEL', "qwen2.5:14b"),
    functions=functions,
    parallel_tool_calls=False,
)

def transfer_to_security_architect():
    return security_architect_agent