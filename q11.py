#Q11: テキストファイル内の文字をアルファベット順に表示せよ。

#split→文字列分割。スペース、改行、タブの場合は引数が不要である。
a = open("q11.txt").read().split()

a.sort() #昇順
#a.sort(reverse=True) #降順では、こう

print(a)