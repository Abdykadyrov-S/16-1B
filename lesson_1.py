
"ООП - Объектно Ориентированное Программирование"
"DRY - Don`t Repeat Yourself == не повторяй себя"

class Car: # Чертеж или шаблон
    "wheels = 4 - Атрибут/свойства/поле класса"
    wheels = 4
    "__init__ - конструктор"
    "self - сам объект"
    def __init__(self, model, color, max_speed):
        "self.model - Атрибут/свойства/поле объекта"
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.is_start = False
        self.tank = 0

    def info(self):
        print(self.model, self.color)

    def start(self):
        self.is_start = True
        print("Машина завелась")

    def stop(self):
        self.is_start = False
        print("Машина приглушена")

    def drive(self, speed):
        if self.is_start == True and self.tank > 0:
            if speed < self.max_speed:
                print(f"машина {self.model} поехала со скоростью {speed} км/ч")
            else:
                print("Вы привысили допусимую скорость машины")
        else:
            print("Машина не заведена или нет топливо")

    def fill(self, value):
        self.tank += value

mersedes = Car("mers", "White", 320)
# print(mersedes.model, mersedes.color)
mersedes.info()
mersedes.fill(10)
mersedes.start()
mersedes.drive(200)
mersedes.stop()

# bmw = Car("bmw", "Pink")
# print(bmw.model, bmw.color)
# bmw.info()




first_super_car = "Car"


FirstSuperCar = "Car"