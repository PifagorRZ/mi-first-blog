import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("minecraft.txt", 'a')
t.write("\n\nPifagor F.P.")

t.close()


printTimeStamp("Pifagor")
