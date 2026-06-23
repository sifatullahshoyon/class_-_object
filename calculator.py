class Calculator:
    brand = 'casio'
    price = 990
    # add
    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1 * num2

num_1 = 14
num_2 = 16

my_cal = Calculator()

addition = my_cal.add(num_1, num_2)
minus = my_cal.sub(num_1, num_2)
multiplication = my_cal.mul(num_1, num_2)
print('Addition : ',addition)
print('Minus : ', minus)
print('Multiplication', multiplication)