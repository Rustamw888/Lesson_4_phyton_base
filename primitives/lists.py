
# Делаем списки!

l = ["string", 123, 2.5, ["another", 321]]
print(l[0])
print(l[1:-1])

print(l)

# Функции списков

l.append("third")
l.extend([1, 2, 2, 2, 3, 4])

l_string = str(l)

assert l.count(2) == 3

print(", ".join(["first", "second", "third"]))

ll = ["first", "second", "third"]
assert len(ll) > 1, f"Длина слишком маленькая! " \
                     f"""Элементы в списке: {', '.join(ll)}"""

print(l)

# Множества

s = set([1, 2, 3, 4, 5, 5, 5, 5])
ss = set([1, 2, 10])

print(s & ss)
print(s | ss)
