#####################################################################################
############################### ------- RULES ------- ###############################
#####################################################################################
#                                                                                   #
# The computer will think of 3 digit number that has no repeating digits.           #
# You will then guess a 3 digit number.                                             #
# The computer will then give back clues.                                           #
# Based on these clues you will guess again until you break the code with a match ! #
#                                                                                   #
# Possible clues :                                                                  #
#   -> close : You've guessed a correct number but in the wrong position.           #
#   -> Match : You've guessed a correct number in correct position.                 #
#   -> Nope : You haven't guess any of the numbers correctly.                       #
#                                                                                   #
#####################################################################################

#!/usr/bin/python
import random

# GET GUESS

def get_guess():
    return list(input("\n[*] What is your guess ?\n"))

# GENERATE COMPUTER CODE

def generate_code():
    digits = [str(num) for num in range(10)]

    # shuffle the digits
    random.shuffle(digits)
    # then grab the first three
    return digits[:3]

# GENERATE CLUES

def generate_clues(code, user_guess):

    if user_guess == code:
        return "CODE CRACKED !"

    clues = []

    for index,num in enumerate(user_guess):
        if num == code[index]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN GAME LOGIC

print("\n\n            Welcome Code Breaker !\n\n")
print('         #############################')
print('         ##   --- CODEBREAKER ---   ##')
print('         ## -- Nope--Close--Match-- ##')
print('         #############################')

print('\n   Clues:')
print("   -> close : You've guessed a correct number but in the wrong position")
print("   -> Match : You've guessed a correct number in correct position")
print("   -> Nope : You haven't guess any of the numbers correctly\n\n")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED !":

    guess = get_guess()

    clue_report = generate_clues(secret_code, guess)
    
    for clue in clue_report:
        print(clue)