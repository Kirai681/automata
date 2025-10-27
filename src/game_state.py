from enum import Enum, auto


class Mode(Enum):
    BUILD = auto()
    RUN = auto()
    PAUSE = auto()


class GameState:
    def __init__(self):
        self.state = Mode.BUILD
        self.state_before = self.state

    def toggle_simulation(self):
        if self.state == Mode.BUILD:
            self.state = Mode.RUN
        elif self.state == Mode.RUN:
            self.state = Mode.BUILD

    def pause(self):
        self.state_before = self.state
        self.state = Mode.PAUSE

    def resume(self):
        if self.state == Mode.PAUSE:
            self.state = self.state_before

    def is_build(self):
        return self.state == Mode.BUILD

    def is_run(self):
        return self.state == Mode.RUN

    def is_paused(self):
        return self.state == Mode.PAUSE

    def current_state(self):
        return self.state
