import random

class PuzzleGenerator:
    def generate(self, difficulty):
        if difficulty == "Easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
        elif difficulty == "Medium":
            a, b = random.randint(10, 50), random.randint(1, 20)
            op = random.choice(["+", "-", "*"])
        else:  # Hard
            a, b = random.randint(20, 100), random.randint(2, 20)
            op = random.choice(["*", "/"])
            if op == "/":
                a = a * b  # ensure clean division

        question = f"{a} {op} {b}"
        answer = eval(question)
        return question, int(answer)
