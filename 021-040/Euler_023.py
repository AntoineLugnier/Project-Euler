import math
import time
start = time.time()

abArr = []

def isAbund (nb):
    global array
    sum = 1
    for i in range (2,int(math.sqrt(nb))+1):
        if nb % i == 0 :
            sum += i
            if i != math.sqrt(nb) :
                sum += nb/i
    if sum > nb :
        return True
    return False

newArray = [True for i in range(28123+1)]
for i in range(1,28123+1) :
    if isAbund(i) :
        abArr.append(i)
        for k in abArr :
            if k + i <= 28123 :
                newArray[k+i] = False
            else :
                break

print('Euler n°23 answer :',sum(k if newArray[k] else 0 for k in range(len(newArray))))
print('Find in :', "%.2f" % (time.time()-start),'sec')
