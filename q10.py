#Q10 Hashnumber 判定
#問題：整数 X の各桁の数字の和を f(X) としたとき、
#　　　X が f(X) で割り切れる場合、X はハーシャッド数です。
#　　　整数 N が与えられるので、ハーシャッド数かどうか判定してください。

n = int(input("Please input integer>"))
s = str(n)
array = list(map(int, list(s))) #list(s)は文字列のリストなので、int型に変換後、その結果をlistにする

x = sum(array)

if n%x == 0:
    print("ハーシャッド数です")
elif n%x != 0:
    print("ハーシャッド数ではありません")
else:
    print("error")