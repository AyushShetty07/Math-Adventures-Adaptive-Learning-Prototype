import time

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def start_timer(self):
        return time.time()

    def log(self, correct, time_taken, difficulty):
        self.records.append({
            "correct": correct,
            "time": time_taken,
            "difficulty": difficulty
        })

    def summary(self):
        total = len(self.records)
        correct = sum(r["correct"] for r in self.records)
        avg_time = sum(r["time"] for r in self.records) / total if total else 0

        return {
            "total_questions": total,
            "accuracy": round((correct / total) * 100, 2),
            "avg_time": round(avg_time, 2)
        }
