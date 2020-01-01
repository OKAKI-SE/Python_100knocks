"""
Q14入れ子のリストを平らにする
問題：[[1,2],3,4,5,[6,[7,[8,9]]]]のように入れ子になっているリストを、
　　　[1, 2, 3, 4, 5, 6, 7, 8, 9]のように平らに入れ直したい。
"""

def flat(ls):
    r = []
    for i in ls:
        if type(i) is list:
            r.extend(flat(i))#appendではない。
        else:
            r.append(i)
    return r

list_nest = [[1,2],3,4,5,[6,[7,[8,9]]]]
print(flat(list_nest))