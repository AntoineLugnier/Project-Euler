import math
import time
start = time.time()

max = 1
index = 1

for i in range (10,1001):
    tInd = 0
    for j in range (math.ceil(i/3),math.ceil(i/2)):
        for k in range(math.ceil(j/2),j):
            if (i-j-k)*(i-j-k) + k*k == j*j :
                tInd += 1
    if tInd > max :
        max = tInd
        index = i

print('Euler n°39 answer :',index)
print('Find in :', "%.2f" % (time.time()-start),'sec')
