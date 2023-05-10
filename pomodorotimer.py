class PomodoroTimer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.paused = False
        self.reps = 0
        self.checks = ""
        self.timer = None

    def start(self):
        self.reps += 1
        reps = self.reps
        self.checks += "💯" * (reps//2)