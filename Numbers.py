# John Asare
# May 9 2020 17:59


""" Answers to udemy Pierian-Data Assessment1"""


# What would you use to find a number’s square root, as well as its square?

def square_root():
    number = int(input('Enter a number to get its square root and square: '))

    square = number ** 2
    square_rt = number ** (1/2)

    print(f'The square of {number} is {square} and the sqrt is {square_rt}')


square_root()

