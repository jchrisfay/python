#Rolls 2 6 side die for each player, compares the results and records the number of times each wins or there is a draw.

from random import randrange

limit = 1000
rolled = 0
firstWins = 0
secondWins = 0
thirdWins = 0
draw = 0

while rolled < limit:

    first = (randrange(6)+randrange(6))
    second = (randrange(6)+randrange(6))
    third = (randrange(6)+randrange(6))


    if third < first > second:
        firstWins = firstWins + 1

    elif first < second > third:
        secondWins = secondWins + 1

    elif first < third > second:
        thirdWins = thirdWins + 1

    else:
        draw = draw + 1

    rolled = rolled + 1

print('First wins ' + str(firstWins))
print('Second wins ' + str(secondWins))
print('Third wins ' + str(thirdWins))
print('Draw ' + str(draw))
