#total = 0
#for i in range(3):  
 #   print " Enter a number please"
   # userInput = int(raw_input())
  #  total = total + userInput
#print total
    
    
    
#totalList = []
#for i in range (5):
 #   print "Enter a number please"
  #  userInput = int(raw_input())
   # totalList.append(userInput)
#print sum(totalList)




num = int(input("Enter a number: "))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print factorial