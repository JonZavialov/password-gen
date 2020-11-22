import random

password = ""

for x in range (10):
    decider = random.randint(0,6)
    if decider == 5 or decider == 6:
        password += str(random.randint(0,9))
    elif decider == 4:
        charDec = random.randint(0,7)
        chars = "!@#$%^&*"
        password += str(chars[charDec])
    elif decider == 1 or decider == 0:
        upLetterDec = random.randint(0,25)
        upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password += upAlpha[upLetterDec]
    else:
        letterDec = random.randint(0,25)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        password += alpha[letterDec]

print("Your password is:", password)
