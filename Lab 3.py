
def printMaxMin(num1,num2,num3):
    if num1 <num2 and num1 < num3:
        print("Num1 is the smallest")
    elif num2<num1 and num2<num3:
        print("num2 is the smallest")
    elif num3<num1 and num3<num2:
        print("num3 is the smallest")
    if num1>num2 and num1 > num3:
            print("Num1 is the greatest")
    elif num2>num1 and num2>num3:
        print("num2 is the greatest")
    elif num3>num1 and num3>num2:
        print("num3 is the greatest")
printMaxMin(1,6,2)







def isEvenOrOdd(num):
    if num % 2 == 0:
        print("Its even")
    else:
        print("Its odd")
        return
num = isEvenOrOdd(3)




