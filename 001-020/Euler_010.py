import math
import time
start = time.time()

array = [True for i in range(2000000)]

def isPrime(nb):
    for i in range (3, int(math.floor(math.sqrt(nb)))+1,2) :
        if nb % i == 0 :
            return False
    return True

total = 2

for i in range(3,2000000, 2) :
    n = 1
    if array[i] :
        total += i
    while n*i < 2000000 :
        array[n*i] = False
        n+=1

print('Euler n°10 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
