
# Учимся писать строки!

s = "i am 'teapot'!"
s = "i am \"teapot\"!"
s = 'i am "teapot"!'
s = """i am ""''teapot!"""
s = '''i am teapot!'''
multiline_string = """first
second
third"""

multiline_string = "first\n" \
                   "second\n" \
                   "third"

print(multiline_string)

print(r"this is stri\ng")

# Индексы и слайсы

s = "abcdefg"
print(s[0])
print(s[1])
print(s[2])

print(s[0:3])
print(s[:-2])
print(s[::-1])



# Оперируем

print("hello, world!".replace("hello", "bye"))
print("hello, world!".replace("o", "0"))
print("hello, world!".split())

assert "hello, world".startswith("Hello")

print("HELLO, world".title())



# Форматируем

first = "first"
second = "second"
third = "third"

print(f"{first} {second} {third.title()} {100}")
print("{2} {1} {0}".format(first, second, third.title()))
print("%s %s %s" % (first, second, third.title()))

s = "(100)"
s = s.replace("(", "").replace(")", "")

assert s.isdigit()
print(100 + int(s))
