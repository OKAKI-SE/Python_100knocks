#Q12: テキストファイル内で指定した文字がいくつ含まれているか数える
#問題：テキストファイルの中に、調べたい文字がいくつ含まれているか自動で数えさせるプログラムを書きなさい。

s=input("input string >")
print(open("q11.txt").read().count(s))
