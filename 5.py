import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


name = input("Твоё имя... ")
print("Darova " + name)


printTimeStamp("Pifagor")