from capitalize import capitalize

if capitalize("hello") != "Hello":
    raise Exception("Функция работает неправильно!")

if capitalize("") != "":
    raise Exception("Функция работает неправильно!")

print("Все тесты пройдены!")
