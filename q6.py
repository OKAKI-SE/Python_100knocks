#FizzBuzz問題
#問題：1〜100までの数字のうち、3で割り切れるものは"Fizz!",5で割り切れるものは"Buzz!",
#15で割り切れるものは"FizzBuzz!"と表示させ、それ以外の数はそのままの数を表示させなさい。　　

#先に大きな数字から処理しないとFizzBuzzが出力されない
for i in range(1,101):
    if i%15 == 0:
        print("FizzBuzz!")
    elif i%3 ==0:
        print("Fizz!")
    elif i%5 ==0:
        print("Buzz!")
    else:
        print(i)