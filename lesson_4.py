" Магические методы - dunder (double underscore) - (методы с двойным подчеркиванием  "


class Computer:
    def __init__(self, name, ssd):  # Вызывается при создании экземпляра класса
        self.name = name
        self.ssd = ssd

    # def info(self):
    #     print(f"{self.name} память - {self.ssd}")
        
    # def __repr__(self): # print 
    #     return f"{self.name} память - {self.ssd} это repr"
    
    def __str__(self):  # print 
        return f"{self.name} память - {self.ssd}"


class Macbook(Computer):
    def __init__(self, name, ssd, cpu):
        super().__init__(name, ssd)
        self.cpu = cpu

    def __str__(self): # print
        return super().__str__() + " " + f"процессор - {self.cpu}, "
    
    "Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции"

    def __call__(self, a, b):
        print("Hello World!")
        print(a + b)

    " Магические методы для арифметических дейчтвий "

    def __add__(self, other): # + 
        new_ssd = self.ssd + other.ssd
        return Macbook(self.name, new_ssd, self.cpu)
    
    def __sub__(self, other): # - 
        new_ssd = self.ssd - other.ssd
        return Macbook(self.name, new_ssd, self.cpu)
    
    def __mul__(self, other): # * 
        new_ssd = self.ssd * other.ssd
        return Macbook(self.name, new_ssd, self.cpu)
    
    def __floordiv__(self, other): # //
        new_ssd = self.ssd // other.ssd
        return Macbook(self.name, new_ssd, self.cpu)
    
    def __truediv__(self, other): # /
        new_ssd = self.ssd / other.ssd
        return Macbook(self.name, new_ssd, self.cpu)

    " Магические методы для операторов сравнения "

    def __gt__(self, other): # больше чем ( > )
        return self.ssd > other.ssd
    
    def __lt__(self, other): # Меньше чем ( < )
        return self.ssd < other.ssd
    
    def __eq__(self, other): # равно ( == )
        return self.ssd == other.ssd
    
    def __ne__(self, other): # не равно ( != )
        return self.ssd != other.ssd
    
    def __ge__(self, other): # больше или равно ( >= )
        return self.ssd >= other.ssd
    
    def __le__(self, other): # меньше или равно ( <= )
        return self.ssd <= other.ssd


mac = Macbook("macbook pro", 512, "M1")
# print(mac)

mac_2 = Macbook("macbook - air", 512, "M2")

" Магические методы для арифметических дейчтвий "
# print(mac + mac_2)
# print(mac - mac_2)
# print(mac * mac_2)
# print(mac // mac_2)
# print(mac / mac_2)


" Магические методы для операторов сравнения "

print(mac > mac_2)
print(mac < mac_2)
print(mac == mac_2)
print(mac != mac_2)
print(mac >= mac_2)
print(mac <= mac_2)
