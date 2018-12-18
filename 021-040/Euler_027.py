import math
import time
start = time.time()

def isPrime(nb):
    for i in range (2, int(math.floor(math.sqrt(nb)))+1) :
        if nb % i == 0 :
            return False
    return True

def nbPrimes(a,b):
    count = 0
    while count*count+a*count+b>0:
        if not isPrime(count*count+a*count+b) :
            break
        else :
            count +=1
    return count

max = 40
value = 41

for a in range(-999,1000) :
    for b in range (-1000,1001) :
        temp = nbPrimes(a,b)
        if temp > max :
            max = temp
            value = a*b

print('Euler n°27 answer :',value)
print('Find in :', "%.2f" % (time.time()-start),'sec')
