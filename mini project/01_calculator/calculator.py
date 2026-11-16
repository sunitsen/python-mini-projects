"""Calculator: classes, __init__, static methods, class methods."""


class Calculator:
    total_calculations = 0  # class variable shared by all instances

    def __init__(self, precision=2):
        self.precision = precision
        self.history = []  # instance variable, unique per calculator

    # ---- static methods: no self/cls, pure helpers ----
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    # ---- class method: works with the class itself ----
    @classmethod
    def supported_operations(cls):
        return {"+": cls.add, "-": cls.subtract, "*": cls.multiply, "/": cls.divide}

    # ---- instance method: uses self state ----
    def calculate(self, a, op, b):
        operations = self.supported_operations()
        if op not in operations:
            raise ValueError(f"Unsupported operator: {op}")
        result = round(operations[op](a, b), self.precision)
        self.history.append(f"{a} {op} {b} = {result}")
        Calculator.total_calculations += 1
        return result
