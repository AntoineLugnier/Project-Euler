import time
start = time.time()

fichier = open("annexes\\Euler_018_annexe.txt", "r")

lines = fichier.read().split("\n")

array = []

for line in lines :
    tempLine = []
    numbers = line.split(" ")
    for number in numbers :
        if number != '' :
            tempLine.append(int(number))
    if len(tempLine) > 0 :
        array.append(tempLine)

def pharaon(x,y,list):
    if y == len(list)-1 :
        return list[y][x]
    else :
        return list[y][x] + max(pharaon(x,y+1,list),pharaon(x+1,y+1,list))

print('Euler n°18 answer :', pharaon(0,0,array))
print('Find in :', "%.2f" % (time.time()-start),'sec')
