class YenToCurrency:
    def __init__(self,yen):
        self.yen = yen

    def doll(self):
        doll = self.yen / 109
        return(doll)

    def euro(self):
        euro = self.yen / 129
        return(euro)

exchange = YenToCurrency(3000)
print('3000円は{}ドルです。'.format(exchange.doll()))
print('3000円は{}ユーロです。'.format(exchange.euro()))