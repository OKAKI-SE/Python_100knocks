#Q8:　為替自動換算クラスの作成
#問題：日本円をドルとユーロに換算するクラスを作成せよ。
#条件：・1ドル=109円, 1ユーロ=129円で換算。(2018/5/8現在)
#　　　・クラスの引数に日本円を入力して、その後その値を各通貨に換算できるようする。

yen = int(input("日本円を入力してください（円） >"))

dollar = yen / 109
euro = yen / 129

print(yen,"円は",round(dollar,2),"ドル")
print(yen,"円は",round(euro,2),"ユーロ")

##下記模範解答
#class YenToCurrency:
#    def __init__(self,yen):
#        self.yen = yen

#    def doll(self):
#        doll = self.yen / 109
#        return(doll)

#    def euro(self):
#        euro = self.yen / 129
#        return(euro)

#exchange = YenToCurrency(3000)
#print('3000円は{}ドルです。'.format(exchange.doll()))
#print('3000円は{}ユーロです。'.format(exchange.euro()))