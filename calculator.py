class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
            
        result = 0
        if b < 0:
            while a >= -b:
                a = self.add(a, b)
                result -= 1
        else:
            while a >= b:
                a = self.subtract(a, b)
                result += 1
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        
        if b < 0:
            b = -b
        if a < 0:
            a = -a

        while a >= b:
            a -= b
        return a
