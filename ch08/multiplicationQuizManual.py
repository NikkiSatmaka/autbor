#!/usr/bin/env python3
# multiplicationQuiz.py

import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    #1: 6 x 8 = 
    #Q: N x N = 
    prompt = f'#{questionNumber + 1}: {num1} x {num2} = '
    start = time.time()  # Mark the start of the question

    for i in range(3):
        try:
            ans = int(input(prompt))
            stop = time.time()  # Mark the time of the answer
            # If it passed 8 seconds when answering, skip to next question
            if stop - start > 8:
                print('Out of time!')
                break
            elif ans == num1 * num2:
                print('Correct!')
                correctAnswers += 1
                break
            # After 3 incorrect tries, put up a notice
            elif i == 2:
                print('Out of tries!')
            else:
                print('Incorrect!')
        except ValueError:
            print('Incorrect!')

    time.sleep(1) # Brief pause to let user see the result.

print(f'Score: {correctAnswers} / {numberOfQuestions}')