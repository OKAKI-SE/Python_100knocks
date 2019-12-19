#Q13: 摂氏と華氏を自動変換
#問題：摂氏（℃）を入力すると華氏（°F）に変換し表示し、
#　　　華氏を入力すると摂氏に変換表示してくれる関数を作成せよ。
#条件：摂氏の場合は"26C"のように入力し、華氏の場合は"67F"のように入力する。

print("気温を入力してください。")
print("※摂氏の場合は26Cのように入力し、華氏の場合は67Fのように入力してください。")
temperature = input(">")

f_str = temperature[-1]
temp = int(temperature[:-1]) #最後の文字を消し、数字のみにする

if f_str == "C" or f_str == "c":
    f = round((temp*9/5)+32,1)
    print("華氏",f,"度です。")
elif f_str == "F" or f_str == "f":
    f = round((temp-32)*5/9)
    print("摂氏",f,"度です。")
else:
    print("正しく入力してください")