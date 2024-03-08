questions_and_answers = {
    'What is the capital of France?': 'Paris',
}

def quiz_user():
    for question, answer in questions_and_answers.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Wrong!")

def main():
    quiz_user()

if __name__ == '__main__':
    main()
