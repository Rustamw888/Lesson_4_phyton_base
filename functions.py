
# Объявляем функции

def func(arg1, arg2, arg3="third"):
    print(arg1, arg2, arg3)


func("hello!", arg2=123, arg3="321")


def upper_string(string: str):
    return string.upper()


print(upper_string("some lowercase"))

# Переменное количество аргументов


def print_all_arguments(*args):
    for arg in args:
        print(arg)


print_all_arguments(1, 2, 3, 4, 5, 6, 7, 8)


def print_all_arguments(end, *args):
    for arg in args:
        print(arg, end=end)


print_all_arguments("", 2, 3, 4, 5, 6, 7, 8)


def print_all_arguments(*args, end="\n"):
    for arg in args:
        print(arg, end=end)


def print_all_arguments_v2(*args, end="\n"):
    print(*args, end=end)


print_all_arguments(2, 3, 4, 5, 6, 7, 8, end="")
print()
print_all_arguments_v2(2, 3, 4, 5, 6, 7, 8, end="\n")


def print_pairs(**kwargs):
    settings = kwargs.pop("settings")
    for key, value in kwargs.items():
        print(key, value)


print_pairs(key="value", some="another", etc=321, settings="fafafa")


d = {"first": 1}
dd = {"second": 2}

ddd = {**d, **dd}

print(ddd)


def f():
    return 1, 2, 3


a, *b = f()

print(a, b)


# Функция - тоже объект

def func():
    pass
