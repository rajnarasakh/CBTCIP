
import random

print("*****************************************************************************************\nRules of the game-\nThis game is played by Computer vs Player.\n1.  Computer starts by setting a random 4-digit number.\n2.  Player takes an attempt at guessing the number.\n3.  If Player succeeds in the first attempt (despite odds which are highly unlikely) \nthey win the game and are crowned MASTERMIND! \n4.  If not, then Computer hints by revealing which digits or numbers Player got correct. \n(Bonus: The correct positions of the numbers Player got right are also revealed.)\n5.  The game continues till Player eventually is able to guess the number entirely.\n6.  At the end of which they are crowned as a true MASTERMIND!\n*****************************************************************************************")

try:
    num = random.randrange(1000, 10000)
    n = int(input("Guess the 4 digit number set by the commputer: "))

    if (n == num):
        print("CONGRATS!!!You got it in the First try, you seem to be a Mastermind!")
    else:
        ctr = 0

        while (n != num):
            ctr += 1
            count = 0

            n = str(n)
            num = str(num)

            correct = ['X']*4
            for i in range(0, 4):
                if (n[i] == num[i]):
                    count += 1
                    correct[i] = n[i]
                else:
                    continue

            if (count < 4) and (count != 0):
                print("Oops!!You didn't get it all, but you did get ",
                      count, " digit(s) correct!")
                print("Correct Numbers from your guess : ")
                for k in correct:
                    print(k, end=' ')
                print('\n')
                print('\n')
                n = int(input("Now try again with the hints given! "))

            elif (count == 0):
                print("OOPS!!Sorry, No Matches!")
                n = int(input("Try Again : "))

        if n == num:
            print("CONGRATS!! You've become a Mastermind!")
            print("You took only", ctr, "tries, Congrats!!")
except ValueError as ve:
    print("Invalid input!!", ve)
