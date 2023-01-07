from decimal import Decimal


def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    summa = (rubles + (coins / 100)) * amount
    return summa


def task_02_sign(number: int) -> int:
    if number > 0:
        return 1
    if number < 0:
        return -1
    if isinstance(number, int | float) != 1:
        return 0


def task_03_trianle(side1: int, side2: int, side3: int) -> bool:
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return 1
    else:
        return 2


def task_04_palindrom(string: str) -> bool:
    string = (string.replace(' ', '')).lower
    rev_string = string[::-1]
    if rev_string == string:
        return 1
    if rev_string != string:
        return 0


x1 = task_01_money(1, 2, 3)
x2 = task_02_sign(4)
x3 = task_03_trianle(1, 2, 3)
x4 = task_04_palindrom("aoa")

print(x1)
print(x2)
print(x3)
print(x4)
