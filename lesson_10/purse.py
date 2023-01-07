class Purse:


    def __init__(self, valute, name = "Unknown"):
        self.__money = 0.00
        self.valute = valute
        self.name = name


    def top_up_balance(self, howmany):
        self.__money += howmany


    def top_down_balance(self, howmany):
        if self.__money >= howmany:
            self.__money -= howmany
        else:
            print("Недостаточно денег")

    def info(self):
        print(self.name, self.__money, self.valute)


    def __del__(self):
        print("Кошелёк удалён")
        return self.__money

x = Purse("USD", "Zhenya")
y = Purse("EUR", "Vanya")
rd = Purse("EUR", "Vanya")
x.__money = -200
x.top_up_balance(10)
x.top_down_balance(1)
y.top_up_balance(25)
x.info()
y.info()
