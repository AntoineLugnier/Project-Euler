import time
start = time.time()

months = [("jan", 31), ("feb", 28), ("mar", 31), ("apr", 30), ("mai", 31), ("jun", 30), ("jul", 31), ("aug", 31), ("sep", 30), ("oct", 31), ("nov", 30), ("dec", 31)]

day = 1

nbSunday = 0

def isLeap(year):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return True
            else :
                return False
        else :
            return True
    else :
        return False

for i in range (1900,2001):
    for month in months:
        if i != 1900 :
            if day % 7 == 0 :
                nbSunday += 1
        if month[0] == "feb" :
            if isLeap(i) :
                day += 1
        day += month[1]

print('Euler n°19 answer :', nbSunday)
print('Find in :', "%.2f" % (time.time()-start),'sec')
