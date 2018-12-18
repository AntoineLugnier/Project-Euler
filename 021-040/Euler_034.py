import time
start = time.time()

def getFacto (nb):
    if nb == 0 :
        return 1
    else :
        pro = 1
        for i in range(1, nb+1) :
            pro *= i
        return pro

total = 0
for i in range (3, 2540160) :
    temp = 0
    for j in range(0,len(str(i))) :
        temp += getFacto(int(str(i)[j]))
        if temp == i :
            total += i

print('Euler n°34 answer :',total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
