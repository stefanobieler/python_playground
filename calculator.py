class Calculator:

    def __init__(self):
        self.answer = 0

    def add(self, *numbers):
        self.answer = 0
        for num in numbers:
            self.answer += num

    def multiply(self, *numbers):
        self.answer = 1
        for num in numbers:
            self.answer *= num



calc = Calculator()

calc.add(1,2,3,4,5)
print(calc.answer)

calc.add(1,2,3,4,5)
print(calc.answer)

calc.multiply(2,2)
print(calc.answer)