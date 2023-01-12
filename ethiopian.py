##완성하진못했지만 연습위해 보내보아요
@@ -1,5 +1,52 @@
import math
result1 = []
result2 = []

#num1 = 146
#num2 = 37

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

decide = {}

# 나누는 함수 recursive로 구현
def e_divide(n: int):
    if n < 2:
        result1.append(n)
    elif n > 1:
        result1.append(n)
        e_divide(math.floor(n/2))

# 곱하는 함수 list comprehension 구현
def e_multply(n: int, count: int) -> list:
    return [n*2**i for i in range(0,count)]

# 판단하는 함수
def e_decision(res1: list, res2: list):
    ans = 0
    #for i in range(len(res1)):
    #  if res1[i]%2!=0:
    #    decide[res1[i]] = res2[i]
    decide = {res1[i]:res2[i] for i in range(len(res1)) if res1[i]%2!=0}
    print(decide)

    for key in decide.keys():
        ans += decide[key]

    return ans

def hello():
    print("Good luck")

if __name__ == '__main__':
    hello()

    e_divide(num1)
    print(result1)

    result2 = e_multply(num2, len(result1))
    print(result2)

    ans = e_decision(result1, result2)
    print(ans)
