# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 20:00 pm
# Solution for problem number 5
# Version 1.0
inputData=input("Please Enter a Positive Integer : ")
inputNum=int(inputData)

if inputNum > 1:
    for i in range(2,inputNum):
        if (inputNum % i) == 0:
            print("This is not Prime")
            break
    else:
        print("This is a Prime")
        

else:
    print ("This is not Prime")

