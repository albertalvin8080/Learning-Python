class Calculator:

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def power(self, a, b):
        return a ** b