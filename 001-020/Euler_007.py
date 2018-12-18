import math
import time
start = time.time()

def isPrime(nb):
    prime = True
    for i in range (2, int(math.floor(math.sqrt(nb)))+1) :
        if nb % i == 0 :
            prime = False
            break
    return prime

nbPrime = 1 #Cause of 2 who is even and isPrime

nb = 1
while nbPrime < 10001 :
    nb += 2
    if isPrime(nb) :
        nbPrime +=1

print('Euler n°7 answer :', nb)
print('Find in :', "%.2f" % (time.time()-start),'sec')
