#FizzBuzz問題
#問題：1〜100までの数字のうち、3で割り切れるものは"Fizz!",5で割り切れるものは"Buzz!",
#15で割り切れるものは"FizzBuzz!"と表示させ、それ以外の数はそのままの数を表示させなさい。　　

cnt_fb = 0
cnt_f = 0
cnt_b = 0

#先に大きな数字から処理しないとFizzBuzzが出力されない
for i in range(1,101):
    if i%15 == 0:
        print("FizzBuzz!")
        cnt_fb += 1
    elif i%3 ==0:
        print("Fizz!")
        cnt_f += 1
    elif i%5 ==0:
        print("Buzz!")
        cnt_b += 1
    else:
        print(i)

print("FizzBuzzは",cnt_fb,"回")
print("Fizzは",cnt_f,"回")
print("Buzzは",cnt_b,"回")
