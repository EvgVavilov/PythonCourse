def f(a):
    def f_2():
        return a*3
    return f_2()
print(f(3))


def outer_func(who):
    def inner_func():
        print(f"Hello, {who}")
    inner_func()
outer_func("World!")


def factorial(number):
    # Валидация входного значения
    if not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")
    # Расчет факториала
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
print(factorial(5))


def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()

print(increment(10))


