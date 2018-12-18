import time
start = time.time()

def removeDigits(nb, rem):
    return str(nb).replace(str(rem),'')

numT = 1
denT = 1

for i in range(10,99) :
    for j in range(i+1,100):
        for k in range(1,10):
            num = removeDigits(i, k)
            den = removeDigits(j, k)
            if num != '' and den != '' and num != '0' and den != '0' and len(num) == 1 and len(den) == 1 :
                if i/j == int(num)/int(den):
                    numT *= i
                    denT *= j

print('Euler n°33 answer :', int(1/(numT/denT)))
print('Find in :', "%.2f" % (time.time()-start),'sec')
