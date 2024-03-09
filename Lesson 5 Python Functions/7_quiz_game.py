
# The Quiz Game

questions_and_answers = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the capital of Spain?": "Madrid",
}

# Task 1: List of Questions and Answers
# Defined above

# Task 2: Quiz Function
def quiz_user():
    score = 0
    for question, answer in questions_and_answers.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    return score

# Task 3: Score and Feedback
def provide_feedback(score):
    print(f"Your score is {score} out of {len(questions_and_answers)}.")

score = quiz_user()
provide_feedback(score)
