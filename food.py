# Script designed to aid in decided what to eat.
import random
#import numpy as np

cheap = ["McDonalds", "Arbys", "Cookout", "Taco Bell", "Waffle House", "Subway", "Captain D's", "Bojangles", "Little Caesar's"]
notcheap = ["O'Charleys", "Chilis", "Chick-fil-a", "Moe's", "Cracker Barrel", "Zaxby's", "Papa John's"]
either = cheap + notcheap
takeoutonly = ["McDonalds", "Arbys", "Cookout", "Taco Bell", "Subway", "Captain D's", "Bojangles", "Little Caesar's", "Chick-fil-a", "Moe's", "Cracker Barrel", "Zaxby's", "Papa John's"]

goodenough = "null"
noblock = ["no"]
#xlast = [0]
#while goodenough is not "no":
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
        length = len(foodlist) - 1
        x = random.randint(1,length)
        #while x in xlast:
                #x = random.randint(1,length)
        #xlast = np.append(xlast, x)
        print("""
You should try""",foodlist[x])
        choices3 = ["yes", "no"]
        goodenough = input("""Would you like another suggestion? Type 'yes' or 'no'
""")
        while goodenough not in choices3:
                print("Please enter 'yes' or 'no' (without apostrophes)")
                goodenough = input("""Would you like another suggestion? Type 'yes' or 'no'
""")

input("""
Press the Enter key to close this window""")
