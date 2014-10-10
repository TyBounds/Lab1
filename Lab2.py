def sum(num1,num2):
    total = num1+num2
    print total

sum(5,4)


def subtract(num3,num4):
    total2 = num3 - num4
    return total2
    
total2 = subtract(8,3)
print total2


def subtractSmaller(num5,num6):
    if num5 > num6:
        #print "Invalid Opperation"
        total3 = num5 - num6
    elif num5 < num6:
        total3 = num6 - num5
    return total3
total3 = subtractSmaller(2,5)