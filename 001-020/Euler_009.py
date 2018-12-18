import math
import time
start = time.time()

for a in range (1,333) :
    for b in range (a+1, int(math.floor((1000-a)/2))):
        c = 1000-b-a
        if a + b + c == 1000 :
            if a*a + b*b == c*c :
                print('Euler n°9 answer :', a*b*c)

print('Find in :', "%.2f" % (time.time()-start),'sec')
