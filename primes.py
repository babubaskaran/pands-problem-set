# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 20:00 pm
# Solution for problem number 5
# Version 1.0
# take user date for positive integer
inputData=input("Please Enter a Positive Integer : ")
# converting input value into integer
inputNum=int(inputData)
#if condition to check value is greater than 1
if inputNum > 1:
    # for loop for input number range
    for i in range(2,inputNum):
        # checking whether its dividing by loop value i
        if (inputNum % i) == 0:
            # print the result
            print("This is not Prime")
            # break the loop
            break
    else:
        # print if the number is prime
        print("This is a Prime")
        

else:
    # print if the value is not prime
    print ("This is not Prime")

