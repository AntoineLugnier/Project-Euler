import math
import time
start = time.time()

number = 600851475143

def isPrime(nb):
    prime = True
    for i in range (2, int(math.floor(math.sqrt(nb)))+1) :
        if nb % i == 0 :
            prime = False
            break
    return prime

for i in range (int(math.floor(math.sqrt(number)))+1, 2, -1) :
    if number % i == 0 :
        if isPrime(i) :
            print('Euler n°3 answer :', i)
            break

print('Find in :', "%.2f" % (time.time()-start),'sec')
