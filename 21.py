import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input())
c = float(n*(n + 1) / 2)
print (c)
printTimeStamp("Pifagor")