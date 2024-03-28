import sqlite3

connect = sqlite3.connect("mbank.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
               id INT PRIMARY KEY,
               full_name VARCHAR (60) NOT NULL,
               email TEXT NOT NULL,
               phone_numbeer INT NOT NULL,
               birth_date DATE,
               pol INT DEFAULT 0,
               balance DOUBLE (7, 2) DEFAULT 0.0
)
""")

class Mbank:
    def __init__(self):
        self.full_name = None
        self.email = None
        self.phone_numbeer = None
        self.birth_date = None
        self.pol = None
        self.balance = 0

    def register(self, full_name, email, phone_numbeer, birth_date, pol):
        self.full_name = full_name
        self.email = email
        self.phone_numbeer = phone_numbeer
        self.birth_date = birth_date
        self.pol = pol
        # cursor.execute("SELECT email FROM clients")
        # if cursor.fetchone() is None:
        cursor.execute(f"""INSERT INTO clients (full_name, email, phone_numbeer, birth_date, pol, balance)
                    VALUES ('{full_name}', '{email}', {phone_numbeer}, '{birth_date}', {pol}, 0.0)""")
        # else:
        #     print("Такая запись уже существует")
        connect.commit()

    def plus(self, amount):
        cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}' ")
        connect.commit()
        self.balance += amount

    def minus(self, amount):
        cursor.execute(f"UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}' ")
        connect.commit()
        self.balance -= amount

    def __str__(self):
        return f"Ваш баланс {self.balance}"
    
    def main(self):
        while True:
            print("Выберите действие:")
            print("0-Выйти, 1-Ренистрация, 2-Пополнить баланс, 3-Снятие денег")
            command = int(input("Введите цифру: "))
            if command == 0:
                break
            elif command == 1:
                full_name = input("Введите свое полное имя: ")
                email = input("Введите свой email: ")
                phone_numbeer = input("Введите свой номер телефона: ")
                birth_date = input("Введите дату рождения: ")
                pol = input("Введите свой пол: ")
                self.register(full_name, email, phone_numbeer, birth_date, pol)

            elif command == 2:
                amount = int(input("Введит сумму для пополнения: "))

                self.plus(amount)
            elif command == 3:
                amount = int(input("Введит сумму для снятия: "))
                self.minus(amount)
            elif command == 4:
                print(self.balance)
mbank = Mbank()
mbank.main()