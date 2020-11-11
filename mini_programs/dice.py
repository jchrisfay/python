# Rolls 2 6 side die for each player, compares the results and records the number of times each wins or there is a draw.

from random import randrange

limit = 100000
rolled = 0
firstWins = 0
secondWins = 0
thirdWins = 0
fourthWins = 0
fifthWins = 0
draw = 0

while rolled < limit:

    first = (randrange(6) + randrange(6))
    second = (randrange(6) + randrange(6))
    third = (randrange(6) + randrange(6))
    fourth = (randrange(6) + randrange(6))
    fifth = (randrange(6) + randrange(6))
    rolls = {"1st": first, "2nd": second, "3rd": third, "4th": fourth, "5th": fifth}
    rolled = rolled + 1

    if min(rolls, key=rolls.get) == "1st":
        firstWins = firstWins + 1
    elif min(rolls, key=rolls.get) == "2nd":
        secondWins = secondWins + 1
    elif min(rolls, key=rolls.get) == "3rd":
        thirdWins = thirdWins + 1
    elif min(rolls, key=rolls.get) == "4th":
        fourthWins = fourthWins + 1
    elif min(rolls, key=rolls.get) == "5th":
        fifthWins = fifthWins + 1

print("First lose :" + str(firstWins))
print("Second lose :" + str(secondWins))
print("Third lose :" + str(thirdWins))
print("Fourth lose :" + str(fourthWins))
print("Fifth lose :" + str(fifthWins))
