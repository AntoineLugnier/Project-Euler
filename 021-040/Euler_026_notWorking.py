from decimal import *
import math
import time
start = time.time()

getcontext().prec = 98

def isCycle(cycle, decimals):
    if len(cycle)>len(decimals):
        return True
    else :
        if (cycle == decimals[0:len(cycle)]):
            return isCycle(cycle, decimals[len(cycle):])

def noUnderCycle(cycle):
    for i in range(0,int(math.floor(len(cycle)/2))):
        if isCycle(cycle[0:i+1],cycle):
            return False
    return True

maxCycle = 6
index = 7
temp = 0

for i in range (8, 1001) :
    analyse = str(Decimal(1)/Decimal(i)).split('.')[1]
    if len(analyse) > 48 :
        for j in range (49,6,-1):
            for k in range(0,48) :
                if k+j < 50 :
                    if noUnderCycle(analyse[k:k+j]) :
                        if isCycle(analyse[k:k+j],analyse) :
                            if j > maxCycle :
                                maxCycle = j
                                index = i
                                temp = analyse
                                break

print(index)
print(temp)
print('Find in :', "%.2f" % (time.time()-start),'sec')
