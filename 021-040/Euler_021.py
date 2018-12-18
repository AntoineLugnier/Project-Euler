import math
import time
start = time.time()

array = []
for i in range (0,10000):
    array.append(None)

def divSum (nb):
    sum = 1
    for i in range (2,int(math.floor(math.sqrt(nb)))+1):
        if nb % i == 0 :
            sum += i
            if i != int(math.sqrt(nb)) :
                sum += nb/i
    return int(sum)

def amicable(nb):
    if divSum(divSum(nb)) == nb :
        return True
    else :
        return False

amiSum = 0

for i in range(2,10000):
    if array[i] == None :
        if amicable(i):
            if divSum(i) < 10000 and i != divSum(i):
                array[i] = True
                array[divSum(i)] = True
        else :
            array[i] = False

    if array[i] == True :
        amiSum += i

print('Euler n°21 answer :', amiSum)
print('Find in :', "%.2f" % (time.time()-start),'sec')
