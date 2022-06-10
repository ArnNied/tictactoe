import utils
from stack import Stack


class History:
    def __init__(self, length):
        self.past = Stack(length)
        self.current = None
        self.future = Stack(length)

    def prev(self):
        if self.current is not None:
            self.future.put(self.current)
        self.current = self.past.get()
        self.show()

        return True

    def next(self):
        if self.current is not None:
            self.past.put(self.current)
        self.current = self.future.get()
        self.show()

        return True

    def do(self, data):
        self.past.put(data)

    def show(self):
        utils.clear_stdout()
        self.current["board"].show()
        print(f"Turn: {self.current['turn']}")
        print(
            f"{self.current['player'].name}({self.current['player'].symbol}) - {self.current['slot']}"
        )

    def exit(self):
        return False

    def start(self):
        loop = True
        while loop:
            valid_action = ["exit"]

            if not self.past.is_empty():
                valid_action.append("prev")

            if not self.future.is_empty():
                valid_action.append("next")

            print(" | ".join([action.upper() for action in valid_action]))
            action = input("> ").lower()

            if action in valid_action:
                loop = getattr(self, action)()
