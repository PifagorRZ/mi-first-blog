import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


summ = 0
summ_num = 0
try:
    while True:
        num = int(input())
        if num == 0:
            print("Ti vvel 0 i programa zakonchilas")
            break
        summ += 1
        summ_num += num
except ZeroDivisionError:
    print("ti vvel 0 pervim simvolom")

print("Srednee znachenie = " + str(summ_num / summ))




printTimeStamp("Pifagor")