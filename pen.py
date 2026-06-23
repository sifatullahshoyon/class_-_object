class Pen:
    manufactured = 'Bangladesh'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

my_pen = Pen('Matador', 10, 'Black')
print(my_pen.brand, my_pen.price, my_pen.color)
my_pen = Pen('Linc', 7, 'Blue')
print(my_pen.brand, my_pen.price, my_pen.color)
my_pen = Pen('Pilot', 5, 'Green')
print(my_pen.brand, my_pen.price, my_pen.color)
