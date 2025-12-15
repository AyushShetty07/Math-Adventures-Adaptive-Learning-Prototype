import streamlit as st
import random
import time

# ------------------ Puzzle Generator ------------------
def generate_puzzle(difficulty):
    if difficulty == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-"])

    elif difficulty == "Medium":
        a, b = random.randint(10, 30), random.randint(1, 20)
        op = random.choice(["+", "-", "*"])

    else:  # Hard
        a, b = random.randint(5, 20), random.randint(2, 10)
        op = random.choice(["*", "/"])
        if op == "/":
            a = a * b  # clean division

    question = f"{a} {op} {b}"
    answer = int(eval(question))
    return question, answer


# ------------------ Adaptive Engine ------------------
def adjust_difficulty(current, recent_results):
    levels = ["Easy", "Medium", "Hard"]
    idx = levels.index(current)

    if len(recent_results) < 3:
        return current

    accuracy = sum(recent_results) / len(recent_results)

    if accuracy >= 0.8 and idx < 2:
        return levels[idx + 1]
    elif accuracy < 0.5 and idx > 0:
        return levels[idx - 1]
    else:
        return current


# ------------------ Session Init ------------------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.q_no = 0
    st.session_state.difficulty = "Easy"
    st.session_state.recent = []
    st.session_state.results = []
    st.session_state.times = []

# ------------------ UI ------------------
st.title("🎯 Math Adventures")
st.subheader("Adaptive Learning Prototype")

# ------------------ Start Screen ------------------
if not st.session_state.started:
    name = st.text_input("Student Name")
    start_level = st.selectbox("Starting Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Start Session"):
        st.session_state.started = True
        st.session_state.name = name
        st.session_state.difficulty = start_level
        st.session_state.q_no = 0
        st.rerun()

# ------------------ Quiz Screen ------------------
elif st.session_state.q_no < 10:
    st.write(f"### Question {st.session_state.q_no + 1} of 10")
    st.write(f"**Difficulty:** {st.session_state.difficulty}")

    if "question" not in st.session_state:
        q, ans = generate_puzzle(st.session_state.difficulty)
        st.session_state.question = q
        st.session_state.answer = ans
        st.session_state.start_time = time.time()

    # 🔥 THIS IS THE PART YOU WERE MISSING
    st.markdown(f"## {st.session_state.question} = ?")

    user_ans = st.text_input("Your Answer", key="ans")

    if st.button("Submit"):
        elapsed = round(time.time() - st.session_state.start_time, 2)

        try:
            correct = int(user_ans) == st.session_state.answer
        except:
            correct = False

        st.session_state.results.append(correct)
        st.session_state.times.append(elapsed)
        st.session_state.recent.append(1 if correct else 0)

        if len(st.session_state.recent) > 3:
            st.session_state.recent.pop(0)

        st.session_state.difficulty = adjust_difficulty(
            st.session_state.difficulty,
            st.session_state.recent
        )

        st.success("Correct!" if correct else f"Wrong! Answer: {st.session_state.answer}")

        st.session_state.q_no += 1

        del st.session_state.question
        del st.session_state.answer
        del st.session_state.start_time

        st.rerun()

# ------------------ Summary Screen ------------------
else:
    st.header("📊 Session Summary")

    accuracy = round((sum(st.session_state.results) / len(st.session_state.results)) * 100, 2)
    avg_time = round(sum(st.session_state.times) / len(st.session_state.times), 2)

    st.write(f"**Student:** {st.session_state.name}")
    st.write(f"**Total Questions:** {len(st.session_state.results)}")
    st.write(f"**Accuracy:** {accuracy}%")
    st.write(f"**Average Response Time:** {avg_time} seconds")
    st.write(f"**Recommended Next Level:** {st.session_state.difficulty}")

    if st.button("Restart"):
        st.session_state.clear()
        st.rerun()
