import os
from flask import Flask, request, make_response
from slack_sdk.signature import SignatureVerifier
from interface.slack.cai_slack_interface import interface
from dotenv import load_dotenv

load_dotenv()

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

app = Flask(__name__)
verifier = SignatureVerifier(signing_secret=SLACK_SIGNING_SECRET)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    payload = request.get_json()
    if payload.get("type") == "url_verification":
        return make_response({"challenge": payload.get("challenge")}, 200)

    if not verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("Invalid signature", 403)

    event = payload.get("event", {})
    print(event)

    if "bot_id" in event:
        return make_response("Ignore bot messages", 200)

    if event.get("type") == "app_mention":
        channel = event["channel"]
        user = event["user"]
        text = event["text"]
        interface.send_reply(channel, f"Hi <@{user}>! You said: `{text}`")
    
    if event.get("type") == "message":
        channel = event["channel"]
        user = event["user"]
        text = event["text"]

        print(f"[Slack] Received message from user {user} in channel {channel}: {text}")
        interface.receive_message(text)

        # Optional: reply to user
        interface.send_reply(channel, f"Hi <@{user}>, you said: `{text}`")

    return make_response("OK", 200)

@app.route("/", methods=["GET"])
def health():
    return "Slack bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)