import signal


class Timeout:

    def __init__(self, seconds: int = 1):
        self.seconds = seconds

    def handle_timeout(self, signum, frame):
        raise TimeoutError

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)
