import math
def prime_factors(number):
    primes = []
    while number > 1:         
        for i in range(2, int(math.sqrt(number))+1):
            while number % i == 0:
                number //= i
                primes.append(i)
        primes.append(number)
        break
    primes = [prime for prime in primes if prime != 1]
    return(primes)
