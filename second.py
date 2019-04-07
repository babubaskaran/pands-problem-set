# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 23:52 pm
# Solution for problem number 9
# Version 1.0
import sys
fileName =sys.argv[1]

#Open the file in read mode
fileOpen=open(fileName,'r')

#open the entire lines in the file
totalLines=fileOpen.readlines()

for i in range(0, len(totalLines)):
    if(i % 2 != 0):
        print(totalLines[i].rstrip('\n'))

fileOpen.close()