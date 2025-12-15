# Math-Adventures-Adaptive-Learning-Prototype
An AI-powered adaptive learning prototype that generates basic math puzzles for children and dynamically adjusts difficulty based on user performance (accuracy and response time), with a simple UI and end-of-session summary.
## Objective
This project demonstrates a minimal AI-powered adaptive learning system for children (ages 5–10) that dynamically adjusts math puzzle difficulty based on user performance.

## Adaptive Logic
A rule-based adaptive engine monitors:
- Recent accuracy (last 3 questions)
- Response time (logged for analysis)

Rules:
- Accuracy ≥ 80% → Increase difficulty
- Accuracy < 50% → Decrease difficulty
- Otherwise → Maintain level

## Difficulty Levels
- Easy: Small numbers, + and -
- Medium: Larger numbers, +, -, *
- Hard: Multiplication and division

## Why Rule-Based?
- Transparent decision-making
- No training data required
- Ideal for prototypes and educational explainability

## How to Run
```bash
python src/main.py
