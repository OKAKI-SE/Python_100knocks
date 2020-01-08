"""
Q18: パスワードを自動生成する
問題：英字（大文字小文字含める）と数字を組み合わせた、8文字のパスワードを自動で生成せよ。
"""

#英字（小文字＆大文字）：string.ascii_letters
#数字：string.digits
#記号：string.punctuation

import string
import random

password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)]) #リストの中の文字を連結
print(password)