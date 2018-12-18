import time
start = time.time()

file = open("annexes\\Euler_022_annexe.txt", "r")

names = file.read().split(",")
names = sorted(names)
total = 0

rank = 0

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for name in names :
    rank += 1
    score = 0
    for i in range (0,len(name)):
        if name[i] in alphabet :
            score += int(ord(name[i]))-64
    total += score*rank

print('Euler n°22 answer :', total)
print('Find in :', "%.2f" % (time.time()-start),'sec')
