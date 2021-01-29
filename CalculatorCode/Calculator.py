class CalculatorMath:
    def __init__(self):
        pass

    def add(self, a, b):
        try:
            result = round(float(a) + float(b),2)
        except ValueError:
            return "加数和被加数需为数字"
        return result

    def div(self, a, b):
        try:
            result = round(float(a) / float(b), 2)
        except ZeroDivisionError:
            return "除数不能为0"
        except ValueError:
            return "除数和被除数必须为数字"
        return result

    def multiply(self, a, b):
        try:
            result = round(float(a) * float(b),2)
        except ValueError:
            return "乘数数和被乘数必须为数字"
        return result
