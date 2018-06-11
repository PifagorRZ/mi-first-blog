import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


x = int(input("God: "))
y = int(input("Mesats: "))
z = int(input("Den: "))
today = datetime.date(x, y, z)
tomorrow = today + datetime.timedelta(days=1)

print("Next day is " + str(tomorrow))

printTimeStamp("Pifagor")