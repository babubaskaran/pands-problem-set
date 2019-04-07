# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 22:00 pm
# Solution for problem number 6
# Version 1.0
# taking input from user to enter a sentence
inputData=input("Please Enter a Sentence : ")
# splitting the input data with a  space and stored into the list
inputlist=inputData.split(' ')
# for condition to check each word position
for i in range(0,len(inputlist)):
    # finding the word on odd position
    if((i%2)==0):
        # print the odd word
        print(inputlist[i])
    
