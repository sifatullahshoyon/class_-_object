
def call():
    print("Calling Someone i don't know")
    return 'call done'

class Phone:
    brand = 'One Plus'
    price = 33000
    color = 'white'
    features = ['camera', 'ram', 'rom', 'speaker']

    def call(self):
        print('calling one person')
    
    def sent_sms(self, phone, sms):
        text = f'sending to sms: {phone} and message: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.sent_sms(68749, 'I forgot to Sent SMS You.')
print(result)