import time
start = time.time()

list = {}

def getPath (x, y):
    global list

    if (x,y) in list :
        return list[(x,y)]

    if y < x :
        x, y = y, x

    if x == 1 and y == 1 :
        list[(x,y)] = 2
        return list[(x,y)]

    if x == y :
        list[(x,y)] = 2*getPath(x-1,y)
        return list[(x,y)]

    if x == 1 :
        list[(x,y)] = 1 + getPath(x,y-1)
        return list[(x,y)]

    list[(x,y)] = getPath(x-1,y) + getPath(x,y-1)
    return list[(x,y)]

print('Euler n°15 answer :', getPath(20,20))
print('Find in :', "%.2f" % (time.time()-start),'sec')
