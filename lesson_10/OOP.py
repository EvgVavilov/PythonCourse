class Purse:

    def __init__(self, number):
        self.money = 0.00 + number
        print("hello")
    def return_self(self, number):
        return self.money + number
x = Purse(2)

print(x.return_self(10))
y = Purse(3)
print(y.return_self(20))
