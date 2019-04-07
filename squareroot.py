# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 22:30 pm
# Solution for problem number 7
# Version 1.0
# taking input from user to enter a sentence
# import math library 
import math
# Getting number from input and converting into float
inputNum=float(input("Please Enter a Positive Number : "))
# assigning variable and calculating square roo of the input number
squarenum = math.sqrt(inputNum)
#print the square root number
print("The square root of", inputNum, "is approx.",round(squarenum,1))