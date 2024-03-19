"Принципы ООП"

class People: # Абстрактный класс и Родительский класс
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def info(self):
        print(f"Имя - {self.name}, {self.age}, {self.hobby}, {self.children}")


class Parents(People): # Родительский класс и Дочерний класс
    def __init__(self, name, age, hobby, children):
       People.__init__(self, name, age, hobby)
       self.children = children

    def info(self):
        print(f"Имя родителя - {self.name}, {self.age}, {self.hobby}, {self.children}")

mother = Parents("Алина", 70, "Voleyboll", 4)
mother.info()


class Child(Parents): # Дочерний класс
    def __init__(self, name, age, hobby, children, study):
        # super().__init__(name, age, hobby, children)
        Parents.__init__(self, name, age, hobby, children)
        self.study = study

    def info(self):
        print(f"Имя ребенка - {self.name}, {self.age}, {self.hobby}, {self.children}, {self.study}")

child = Child("Айдай", 13, "Footbal", False, "Geeks")
child.info()

