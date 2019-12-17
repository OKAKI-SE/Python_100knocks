#0から100の内３の倍数と３のつく数字だけ表示せよ。
for i in range(101):
    if "3" in str(i) or i%3 == 0: 
        print(i)
        i+=1