
# Заводим словарики

d = {
    "key": "value",
    123: "another",
    10: {"another": "first"},
}

print(d["key"])

print(list(d.keys()))
print(list(d.values()))

# Функции словарей

print(list(d.items()))

d["first"] = "some string"

print(d)

value = d.pop("first")
