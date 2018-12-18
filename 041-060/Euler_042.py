import time
start = time.time()

def isTriangle(nb):
    n = 0
    incr = 1
    while True :
        n += incr
        incr += 1
        if nb == n :
            return True
        elif nb < n :
            return False

fichier = open("annexes\\Euler_042_annexe.txt")
mots = fichier.read().replace('"','').replace('\n','').split(',')

nbTri = 0
for mot in mots :
    score = 0
    if mot != '' :
        for i in range (0,len(mot)) :
            score += ord(mot[i])-64
        if isTriangle(score) :
            nbTri += 1

print('Euler n°42 answer :',nbTri)
print('Find in :', "%.2f" % (time.time()-start),'sec')
