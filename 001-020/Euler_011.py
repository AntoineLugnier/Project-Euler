import time
start = time.time()

file_number = open("annexes\\Euler_011_annexe.txt", "r")

lines = file_number.read().split("\n")

array = []

max = 0

for line in lines :
    temp = []
    numbers = line.split(" ")
    for number in numbers :
        try :
            temp.append(int(number))
        except:
            True
    if(len(temp)>0):
        array.append(temp)

tempSum = 1
for i in range (0,len(array[0])):
    for j in range(0,len(array)):
        if i <= len(array[0])-4 :
            tempSum = 1
            for tempI in range(0,4):
                tempSum *= array[j][i+tempI]
            if tempSum > max :
                max = tempSum

        if j < len(array)-4 :
            if i < len(array[0])-4 :
                tempSum = 1
                for tempI in range(0,4):
                    tempSum *= array[j+tempI][i+tempI]
                if tempSum > max :
                    max = tempSum
            if i >= 3 :
                tempSum = 1
                for tempI in range(0,4):
                    tempSum *= array[j+tempI][i-tempI]
                if tempSum > max :
                    max = tempSum
            tempSum = 1
            for tempI in range(0,4):
                tempSum *= array[j+tempI][i]
            if tempSum > max :
                max = tempSum

print('Euler n°11 answer :', max)
print('Find in :', "%.2f" % (time.time()-start),'sec')
