from queue import Queue, Empty
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()

class CAISlackInterface:
    """
    Handles input/output communication between a Slack channel and the CAI agent.
    """

    def __init__(self, slack_token: str, timeout: int = 60):
        self.client = WebClient(token=slack_token)
        self.input_queue = Queue()
        self.timeout = timeout
        self.thread = None
        self.agent = None
        self.running = False

    def receive_message(self, message: str):
        """Receive input from Slack (e.g., from webhook handler)."""
        self.input_queue.put(message)

    def get_user_message(self, *args, **kwargs) -> str:
        """Called by run_cai_cli. Waits for user input via Slack."""
        try:
            print("[CAISlackInterface.get_user_message] Waiting for user input...")
            return self.input_queue.get()
        except Empty:
            print("[CAISlackInterface.get_user_message] No input received, returning 'exit'.")
            return "exit"

    def send_reply(self, channel_id: str, message: str):
        """Send message back to Slack."""
        try:
            response = self.client.chat_postMessage(
                channel=channel_id,
                text=message
            )
            print(f"[CAISlackInterface.send_reply] Sent to {channel_id}: {message}")
        except SlackApiError as e:
            print(f"[CAISlackInterface.send_reply] Slack API error: {e.response['error']}")
        except Exception as ex:
            print(f"[CAISlackInterface.send_reply] Unexpected error: {ex}")

interface = CAISlackInterface(
    slack_token=os.environ["SLACK_BOT_TOKEN"],
    timeout=60
)