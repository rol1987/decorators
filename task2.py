import os
from datetime import datetime

# 2 Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает
# в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать
# без ошибок.

def logger2(path):
    def __logger2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, "a") as log_file:
                log_file.write(f"{datetime.now()} - {old_function.__name__} - {args} - {kwargs} - {result}\n")

            return result

        return new_function

    return __logger2

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        # if os.path.exists(path):
        #     os.remove(path)

        @logger2(path)
        def hello_world():
            return 'Hello World'

        @logger2(path)
        def summator(a, b=0):
            return a + b

        @logger2(path)
        def div(a, b):
            return a / b

        result1 = hello_world()
        result2 = summator(2, 2)
        result3 = div(6, 2)

        summator(4.3, b=2.2)
        summator(a=0, b=0)

if __name__ == '__main__':
    test_2()