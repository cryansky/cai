from queue import Queue
from threading import Thread

class SlackSession:
    def __init__(self, user_id: str, say_fn):
        self.user_id = user_id
        self.say_fn = say_fn
        self.input_queue = Queue()
        self.thread = None
        self.running = False

    def receive_message(self, message: str):
        self.input_queue.put(message)

    def get_user_message(self, *args, **kwargs):
        return self.input_queue.get()

    def send_reply(self, message: str):
        self.say_fn(text=message)

    def start_agent(self, agent_runner_class):
        if self.running:
            return

        def agent_loop():
            self.running = True
            runner = agent_runner_class(self)
            runner.run_loop() 
            self.running = False

        self.thread = Thread(target=agent_loop, daemon=True)
        self.thread.start()

class SlackSessionManager:
    def __init__(self):
        self.sessions = {}

    def get_or_create_session(self, user_id, say_fn):
        if user_id not in self.sessions:
            self.sessions[user_id] = SlackSession(user_id, say_fn)
        else:
            # Update say_fn on every new message for the session
            self.sessions[user_id].say_fn = say_fn
        return self.sessions[user_id]