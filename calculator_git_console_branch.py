class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        result = self.number1 + self.number2
        print(f"{self.number1} + {self.number2} = {result}")
        return

    def subtraction(self):
        result = self.number1 - self.number2
        print(f"{self.number1} - {self.number2} = {result}")
        return

    def multiplication(self):
        result = self.number1 * self.number2
        print(f"{self.number1} * {self.number2} = {result}")
        return

    def division(self):
        if self.number2 == 0:
            print("На 0 ділити не можна")
            return
        else:
            result = self.number1 / self.number2
            print(f"{self.number1} / {self.number2} = {result}")
            return

while True:
    number1=input("Введіть перше число - ")
    if number1.isalpha():
        print("Некоректний ввод. Введіть число")
        continue
    else:
        number1=float(number1)
        break

while True:
    number2=input("Введіть друге число - ")
    if number2.isalpha():
        print("Некоректний ввод. Введіть число")
        continue
    else:
        number2=float(number2)
        break

while True:
    action=input("Введіть потрібну дію (+, -, *, /) ")
    if action == "+":
        Calculator(number1,number2).addition()
        break
    elif action == "-":
        Calculator(number1,number2).subtraction()
        break
    elif action == "*":
        Calculator(number1,number2).multiplication()
        break
    elif action == "/":
        Calculator(number1,number2).division()
        break
    else:
        print("Некоректний ввод. Виберіть потрібну дію (+, -, *, /) ")
        continue