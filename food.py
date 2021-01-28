# Script designed to aid in decided what to eat.
import random

cheap = ["McDonalds", "Subway", "Little Caesar's"]
notcheap = ["O'Charleys", "Chilis", "Moe's"]
either = cheap + notcheap
takeoutonly = ["McDonalds", "Subway", "Little Caesar's"]

goodenough = "null"
noblock = ["no"]

while goodenough not in noblock:
        choices = ["in", "out"]
        takeoutoreatin = input("""Dine in or take out? Type 'in' or 'out'
""")
        while takeoutoreatin not in choices:
                print("Please enter 'in' or 'out' (without apostrophes)")
                takeoutoreatin = input("""Dine in or take out? Type 'in' or 'out'
""")
        if takeoutoreatin == "out":
                foodlist = takeoutonly
        else:
                choices2 = ["cheap", "notcheap", "either"]
                cheapornot = input("""Cheap, not as cheap, or either? Type 'cheap', 'notcheap', or 'either'
""")
                while cheapornot not in choices2:
                        print("Please enter 'cheap', 'notcheap', or 'either' (without apostrophes or commas)")
                        cheapornot = input("""Cheap, not as cheap, or either? Type 'cheap', 'notcheap', or 'either'
""")
                if cheapornot == "cheap":
                        foodlist = cheap
                if cheapornot == "notcheap":
                        foodlist = notcheap
                if cheapornot == "either":
                        foodlist = either
        #length = len(foodlist) - 1 # Old way of doing it
        #x = random.randint(1,length)
        random.shuffle(foodlist)
        if foodlist == []:
                print("""
You have seen all available restaurants for the options given.
If you would like to see them again, please choose 'no' and reboot the script.""")
        else:
                print("""
You should try""",foodlist.pop()) # used to be foodlist[x]
        choices3 = ["yes", "no"]
        goodenough = input("""Would you like another suggestion? Type 'yes' or 'no'
""")
        while goodenough not in choices3:
                print("Please enter 'yes' or 'no' (without apostrophes)")
                goodenough = input("""Would you like another suggestion? Type 'yes' or 'no'
""")

input("""
Press the Enter key to close this window""")
exit()
