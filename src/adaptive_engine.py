class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def next_difficulty(self, current, recent_results):
        if len(recent_results) < 3:
            return current

        accuracy = sum(recent_results) / len(recent_results)

        idx = self.levels.index(current)

        if accuracy >= 0.8 and idx < 2:
            return self.levels[idx + 1]   # Increase difficulty
        elif accuracy < 0.5 and idx > 0:
            return self.levels[idx - 1]   # Decrease difficulty
        else:
            return current
