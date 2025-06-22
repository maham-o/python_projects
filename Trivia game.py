# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell teh user their score
import random
questions = {
    "What is the keyword to define a function in Python?": 'def',
    "Which data type is used to store True of False values?": 'boolean',
    "What is the correct file extension for Python files?": '.py',
    "Which symbol is used to comment in Python?": '#'
}


def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 4
    score = 0
    selected_questions= random.sample(questions_list,total_questions)
    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")

    print(f"Game over! Your final score is: {score}/{total_questions}")

python_trivia_game()