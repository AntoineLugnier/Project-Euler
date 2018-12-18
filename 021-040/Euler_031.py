import time
start = time.time()

pieces = [1,2,5,10,20,50,100,200]

def getComb (nb, max) :
    global pieces
    total = 0
    for piece in pieces :
        if piece <= max :
            if piece < nb :
                total += getComb(nb-piece, piece)
            else :
                if piece == nb :
                    total += 1
                break
    return total

print('Euler n°31 answer :',getComb(200, 200))
print('Find in :', "%.2f" % (time.time()-start),'sec')
