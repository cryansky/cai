"""Security Architect Base Agent"""
import os
from dotenv import load_dotenv
from cai.sdk.agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from cai.util import load_prompt_template  # Add this import

load_dotenv()
model_name = os.getenv("CAI_MODEL", "alias0")

from cai.tools.reconnaissance.generic_linux_command import (  # pylint: disable=import-error # noqa: E501
    generic_linux_command
)

from cai.tools.reconnaissance.exec_code import (  # pylint: disable=import-error # noqa: E501
    execute_code
)

from cai.tools.web.search_web import (  # pylint: disable=import-error # noqa: E501
    make_web_search_with_explanation,
)

from cai.tools.vendors.atlassian import ( # pylint: disable=import-error # noqa: E501
    read_confluence_page,
    write_confluence_inline_comment,
    read_confluence_inline_comments,
    reply_to_confluence_comment,
    write_confluence_footer_comment,
    search_confluence
)

# Prompts
security_architect_agent_system_prompt = load_prompt_template("prompts/system_security_architect_agent.md")

# Define tools list based on available API keys
tools = [
    generic_linux_command,
    execute_code,
    read_confluence_page,
    write_confluence_inline_comment,
    read_confluence_inline_comments,
    reply_to_confluence_comment,
    write_confluence_footer_comment,
    search_confluence
]

if os.getenv('PERPLEXITY_API_KEY'):
    tools.append(make_web_search_with_explanation)

security_architect_agent = Agent(
    name="Security Architect Agent",
    description="""Agent that specializes in gathering knowledge from design review documents.
                   Expert in identifying potential vulnerability and security risk based on design documents.""",
    instructions=security_architect_agent_system_prompt,
    tools=tools,
    model=OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=AsyncOpenAI(),
    ),
)