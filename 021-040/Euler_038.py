import time
start = time.time()

def isPande (strNb):
    for i in range(1,10):
        if not str(i) in strNb :
            return False
    return True

max = 0

for n in range(2,10):
    for i in range(1,10000):
        strNb = ''
        for j in range(1, n+1):
            strNb += str(i*j)
        if len(strNb) == 9 :
            if isPande(strNb):
                if int(strNb) > max :
                    max = int(strNb)
        elif len(strNb) > 9 :
            break

print('Euler n°38 answer :',max)
print('Find in :', "%.2f" % (time.time()-start),'sec')
