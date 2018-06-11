import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

latters = ['a', 'e', 'i', 'o', 'u']
user = input("Vvedite bukvu ")
if user in latters:
    print("You bukva golosna")
elif user == 'y':
    print("You bukva mozet bit i golozna i prigolosna")
else:
    print("You bukva is prigolosna")

printTimeStamp("Pifagor")