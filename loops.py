
# While

i = 8
while i < 10:
    print("something " + str(i))
    i += 1

# For

l = ["first", "second", "third"]

for element in l:
    print(element)


for element in "this is string":
    print(element, end="")


from primitives.dicts import d

print("\n=====================")

for key, item in d.items():
    print(key, item, sep=" | ")


l = ["first", "second", "third"] * 5

for i in range(3, len(l) + 1):
    print(l[i])
