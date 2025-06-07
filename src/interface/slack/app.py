import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from queue import Queue
from interface.slack.slack_session import SlackSessionManager
from interface.slack.agent_runner import CAISlackAgentRunner

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

session_manager = SlackSessionManager()

@app.event("message")
def handle_message_events(body, say):
    user = body["event"].get("user")
    text = body["event"].get("text")
    channel = body["event"].get("channel")

    if not user or not text:
        return

    say(f"<@{user}>: Got your message! Processing...")

    session = session_manager.get_or_create_session(user, say)
    session.receive_message(text)
    session.start_agent(CAISlackAgentRunner)

    session.send_reply("Done processing.")

if __name__ == "__main__":
    # HTTP Mode
    app.start(3000)
    
    # Socket Mode
    # handler = SocketModeHandler(app, os.environ["SLACK_BOT_TOKEN"])
    # handler.start()