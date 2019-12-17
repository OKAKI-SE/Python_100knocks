# 2つの自然数の最小公倍数/最大公約数を表示せよ
import math

a = int(input("a >"))
b = int(input("b >"))

def lcm(a,b):
    return (a*b) // math.gcd(a,b)

print("lcm:",lcm(a,b)) #最小公倍数（least common multiple）
print("gcd:",math.gcd(a,b)) #最大公約数（greatest common divisor）
