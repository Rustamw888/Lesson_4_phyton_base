# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def function_print_name(function_name):
    new_name = function_name.__name__.replace("_", " ").capitalize()
    new_arguments = replace_function(function_name)
    if len(new_arguments) > 0:
        print(f"{new_name}: {new_arguments}")
    else:
        print(new_name)


def replace_function(function_name):
    arguments = str(function_name.__code__.co_varnames)
    for symbol in ["(", ")", "'", ","]:
        if symbol in arguments:
            arguments = arguments.replace(symbol, "")
    return arguments.replace("_", " ")


def open_browser(browser_name):
    function_print_name(open_browser)


def go_to_companyname_homepage(page_url):
    function_print_name(go_to_companyname_homepage)


def find_registration_button_on_login_page(page_url, button_text):
    function_print_name(find_registration_button_on_login_page)


open_browser("browser_name")
go_to_companyname_homepage("page_url")
find_registration_button_on_login_page("page_url", "button_text")
