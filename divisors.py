# Author : Babu Baskaran 
# Date   : 06/04/2019 Time : 13:00 pm
# Solution for problem number 3
# Version 1.0

for i in range(1000, 1100):
#  for i2 in range(1000, 10000):
 #   div1 = i / 6
  #  div2 = i /12
   # res2 = div2 % 2
    #res1 = div1 % 2
  if (i % 6 == 0) and (i % 12 != 0): 
    print (i)
