# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 23:52 pm
# Solution for problem number 9
# Version 1.0
# Importing sys funtion
import sys
#assigning  file name into variable
fileName =sys.argv[1]

#Open the file in read mode
fileOpen=open(fileName,'r')

#open the entire lines in the file
totalLines=fileOpen.readlines()
#for loop to get every 2nd line
for i in range(0, len(totalLines)):
    # if condition to check not equal to zero    
    if(i % 2 != 0):
        #print lines    
        print(totalLines[i].rstrip('\n'))

fileOpen.close()