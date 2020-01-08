"""
Q17: 16進数ダンプ(逆バージョンも)
16進数ダンプとは、メモリーやファイルの内容などを16進数の形で目に見えるように書き出す（表示する）こと
"""
import binascii

#string = input("文字列を入力してください >") #文字列→16進数の時のみ、標準入力からできなかった・・・
num = input("16進数を入力してください(ex.48656c6c6f) >")
print(binascii.hexlify(b'hello'))
print(binascii.unhexlify(num))
