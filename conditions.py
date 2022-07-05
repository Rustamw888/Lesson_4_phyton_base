
# Boolean

t = True
f = False


# if/elif/else

if True:
    print("It's true!")

if not False:
    print("It's false!")

b = True or False
if b:
    print("something")

if 0:
    print("zero")

if "":
    print("empty")

if None:
    print("None")


import random

b = random.randint(0, 1)
if b:
    print("Got it!")
else:
    print("Nope")

b = random.randint(0, 2)

if b == 0:
    print("Zero")
elif b == 1:
    print("One")
else:
    print("Something else")
