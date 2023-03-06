# !/usr/bin/env python3
import operator
import prompt
from random import randint


def welcome_user_calc():
    print('brain-calc')
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')

    print('What is the result of the expression?')
    return names


name = welcome_user_calc()

def types_operation():
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)

    result = randint(0, 2)

    if result == 0:
        result_expression = (number_1 + number_2)
        operations = '+'
    elif result == 1:
        result_expression = (number_1 - number_2)
        operations = '-'
    else:
        result_expression = (number_1 * number_2)
        operations = '*'

    print('Question:', number_1, operations, number_2)
    return result_expression


result_expressions = types_operation()

def checking_answers():
    answer = int(input('Your answer: '))

    if answer == result_expressions:
        print('Correct!')
    else:
        print(f"'{answer}'", "is wrong answer ;(. "
                             "Correct answer was", f"'{result_expressions}'" + ". "
                             "Let's try again,", name + "!")


checking_answers()
