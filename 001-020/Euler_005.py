import time
start = time.time()

stop = False
nb = 2520

while not stop :
    for i in range (11,21) :
        if nb % i != 0 :
            break
        else :
            if i == 20 :
                stop = True
                print('Euler n°5 answer :', nb)
    nb += 420

print('Find in :', "%.2f" % (time.time()-start),'sec')
