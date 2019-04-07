# Author : Babu Baskaran 
# Date   : 06/04/2019 Time : 13:00 pm
# Solution for problem number 3
# Version 1.0

# assigning range of numbers from 1000 to 10000 in for loop
for i in range(1000, 10000):
  # checking if the range of number is divided by 6 but not divided by 12
  if (i % 6 == 0) and (i % 12 != 0): 
    # print the result of collatz
    print (i)