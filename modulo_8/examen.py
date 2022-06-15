class Uno():
    def muestra(self):
        return 2022
    def taco_1(self):
        return self.muestra()

class Dos(Uno):
    def muestra(self):
        return 'OOP'
    def taco_4(self):
        return 'Hello'



p_1 = Uno()
p_2 = Dos()
print(p_1.muestra())
print(p_1.taco_1())
print(p_2.muestra())
print(p_2.taco_1())
