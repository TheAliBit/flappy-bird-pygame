class Boundary:
    def __init__(self, screen, state):
        self.top = (0, 0, screen.get_width(), 10)
        self.state = state

    # def run(self):
    #     if self.state["playing"]:
    #         self.
