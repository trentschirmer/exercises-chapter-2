from math import sqrt

def isprime(number: int)->bool:
    
    prime = True
    if number == 1:
        prime = False

    i = 2
    while i <= sqrt(abs(number)) and prime:
        if number % i == 0:
            prime = False
        i+=1
    return prime

