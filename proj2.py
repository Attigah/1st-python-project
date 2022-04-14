import random

yourRandnum = random.randrange(-10, 26)

highest_range = input("Type a number: ")
if highest_range.isdigit():
    highest_range = int(highest_range)

    if highest_range <= 0:
        print("please type a number higher than 0 ")
        quit()


else:
    print("please type a number next time ")
    quit()



