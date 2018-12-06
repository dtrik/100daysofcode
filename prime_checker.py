import math

def is_prime(num):
    if num == 1:
        return("Not prime")
    if num != 2 and num % 2 == 0:
        return("Not prime")
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return("Not prime")
    return("Prime")

T = int(input())
for i in range(T):
    num = int(input())
    print(is_prime(num))