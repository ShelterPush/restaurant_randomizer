# Script designed to aid in deciding what to eat.
import random

cheap = ["McDonalds", "Arbys", "Cookout", "Taco Bell", "Waffle House", "Subway", "Captain D's", "Bojangles", "Little Caesar's"]
notcheap = ["O'Charleys", "Chilis", "Chick-fil-a", "Moe's", "Cracker Barrel", "Zaxby's", "Papa John's"]
either = cheap + notcheap
takeoutonly = ["McDonalds", "Arbys", "Cookout", "Taco Bell", "Subway", "Captain D's", "Bojangles", "Little Caesar's", "Chick-fil-a", "Moe's", "Cracker Barrel", "Zaxby's", "Papa John's"]

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
    choices2 = ["cheap", "notcheap"]
    cheapornot = input("""Cheap, or not as cheap? Type 'cheap' or 'notcheap'
""")
    while cheapornot not in choices2:
        print("Please enter 'cheap' or 'notcheap' (without apostrophes)")
        cheapornot = input("""Cheap, or not as cheap? Type 'cheap' or 'notcheap'
""")
    if cheapornot == "cheap":
        foodlist = cheap
    else:
        foodlist = notcheap
length = len(foodlist) - 1
x = random.randint(1,length)
print("""
You should try""",foodlist[x])
input("""
Press the Enter key to close this window""")
