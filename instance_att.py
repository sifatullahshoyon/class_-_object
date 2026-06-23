class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mez jab eeen')
mehjabeen.add_to_cart('shoe')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('Arfan Nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('car')
print(nisho.cart)

shoyon = Shop('Sifat Ullah Shoyon')
shoyon.add_to_cart('Jursey')
print(shoyon.cart)