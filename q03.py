#フィボナッチ数列（１０個目まで）を表示せよ

#f = [1,2,3,4,5,6,7,8,9,10]
#n=0
#for n in range(10):
#    result = int(f[n-2]) + int(f[n-1])
#    print(result)

a = 0
b = 1
for i in range(10):
    print(b)
    a, b = b, a+b