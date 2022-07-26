print("""
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
""")

positive = 1
negative = 2

def main():

    score = 0
    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(1, answer)

    print("2. I feel that I have a number of good qualities.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(1, answer)

    print("3. All in all, I am inclined to feel that I am a failure.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(2, answer)

    print("4. I am able to do things as well as most other people.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(1, answer)

    print("5. I feel I do not have much to be proud of.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(2, answer)

    print("6. I take a positive attitude toward myself.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(1, answer)

    print("7. On the whole, I am satisfied with myself.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(1, answer)

    print("8. I wish I could have more respect for myself.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(2, answer)

    print("9. I certainly feel useless at times.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(2, answer)

    print("10. At times I think I am no good at all.")
    answer = input("Enter D, d, a, or A: ")
    score += compute_score(2, answer)

    print(f'\nYour score is {score}')
    print('A score below 15 may indicate problematic low self-esteem.\n')

def compute_score(pos_or_neg, response):

    if pos_or_neg == 1 and response == 'D':
        points = 0
    elif pos_or_neg == 1 and response == 'd':
        points = 1
    elif pos_or_neg == 1 and response == 'a':
        points = 2
    elif pos_or_neg == 1 and response == 'A':
        points = 3
    elif pos_or_neg == 2 and response == 'D':
        points = 3
    elif pos_or_neg == 2 and response == 'd':
        points = 2
    elif pos_or_neg == 2 and response == 'a':
        points = 1    
    elif pos_or_neg == 2 and response == 'A':
        points = 0

    return points

main()


