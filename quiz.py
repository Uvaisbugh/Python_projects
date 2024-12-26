import random
import time

quiz = {
    1: {'question': 'What is the capital of France?', 'answer': 'Paris'},
    2: {'question': 'What is 2 + 2?', 'answer': '4'},
    3: {'question': 'What is the color of the sky?', 'answer': 'Blue'},
    4: {'question': 'What is the capital of Spain?', 'answer': 'Madrid'},
    5: {'question': 'What is 3 * 3?', 'answer': '9'},
    6: {'question': 'What is the color of grass?', 'answer': 'Green'},
    7: {'question': 'What is the capital of Italy?', 'answer': 'Rome'}
}

score = 0
questions = list(quiz.values())
random.shuffle(questions)

for value in questions:
    print(value['question'])
    start_time = time.time()
    answer = input("Answer: ")
    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time > 10:
        print("Time's up! You took too long to answer.")
    elif answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])

    print("Your score is: " + str(score))
    print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")

if score == 7:
    print("Excellent! You got all questions right!")
elif score >= 5:
    print("Good job! You scored well.")
else:
    print("Better luck next time!")