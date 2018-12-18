import time
start = time.time()

base = [0,1,2,3,4,5,6,7,8,9]

count = 0

def getPermu(nbs, stri):
    global count
    if len(nbs) == 1 :
        count += 1
        if count == 1000000 :
            print('Euler n°24 answer :',stri+str(nbs[0]))
            return True
    else :
        for nb in nbs :
            nbs2 = nbs.copy()
            nbs2.remove(nb)
            if getPermu(nbs2,stri+str(nb)) :
                return True
    return False

getPermu(base, '')
print('Find in :', "%.2f" % (time.time()-start),'sec')
