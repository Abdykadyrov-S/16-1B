# "Принципы ООП"

# # def info():
# #     print("parent")

# # def info():
# #     print("child")

# # info()
# # info()
# # info()

# # number = 3

# # number = 5

# # print(number)

# "Полиморфизм"

# # class Animals:
# #     def make_sound(self):
# #         print("ksss")

# # class Cat(Animals):
# #     def make_sound(self):
# #         print("MEOW!")

# # class Dog(Animals):
# #     def make_sound(self):
# #         print("Gaf-Gaf!")

# # murka = Cat()
# # murka.make_sound()

# # bob = Dog()
# # bob.make_sound()


# "Инкапсуляция"

# class SmartPhone:
#     def __init__(self, model, color, memory):
#         self.model = model # Публичный
#         self._color = color # Защищенным
#         self.__memory = memory # Приватный

#     " @ - Декоратор "
#     @property
#     def memory(self):
#         return self.__memory

#     def info(self): # Публичный
#         print(f"Телефон - {self.model}, {self._color}, {self.__memory} ")
    
#     def _messanger(self): # Защищенным
#         print("Whatsapp")

#     def __reset_password(self):  # Приватный
#         print("Сброс пароля")

#     @property
#     def reset_password(self):
#         return self.__reset_password

# samsung = SmartPhone("A20", "Black", 256)
# # print(samsung.model)
# # print(samsung._color)
# print(samsung.memory)
# # samsung.info()
# samsung.info()
# samsung.reset_password()


def sary(func):
    def tash():
        print("hello World!")
        print("Bye!")
        func()
    return tash

@sary
def add():
    print(2 + 2)

add()


"Множественное наследование "


class People: # Абстрактный класс и Родительский класс
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def info(self):
        print(f"Имя - {self.name}, {self.age}, {self.hobby}")


class Father(People):
    def __init__(self, name, age, hobby, job):
        People.__init__(self, name, age, hobby)
        self.job = job

class Mother(People):
    def __init__(self, name, age, hobby, cooking):
        People.__init__(self, name, age, hobby)
        self.cooking = cooking

class Child(Father, Mother):
    def __init__(self, name, age, hobby, job, cooking):
        Father.__init__(self, name, age, hobby, job)
        Mother.__init__(self, name, age, hobby, cooking)

    def info(self):
        print(f"Имя - {self.name}, {self.age}, {self.hobby}, {self.cooking}, {self.job}")


child = Child("Нурислам", 15, " - ", False, True)

child.info()