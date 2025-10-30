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