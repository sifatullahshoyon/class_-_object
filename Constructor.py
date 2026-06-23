class Phone:
    manufactured = 'China'
    # Constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sent_sms(self, phone, sms):
        text = f'Sending to: {phone} {sms}'
        print(text)
    

my_phone = Phone('Sifat', 'one plus', 33000)
print(my_phone.owner, my_phone.brand, my_phone.price)

father_phone = Phone('My Father Phone', 'Walton', 15000)
print(father_phone.owner, father_phone.brand, father_phone.price)

result = my_phone.sent_sms('sms in', 'my phone')
print(result)