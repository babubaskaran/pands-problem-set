# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 22:55 pm
# Solution for problem number 8
# Version 1.0
# import the datetime of the system using import syntax
#import time 

import time 
  
b = time.strftime("%A, %B %d %Y at %I:%M%p")
print(b)

# checking the weekday number is equal to 1 using if condition
# if datetime.datetime.today().weekday() == 1: 
#     # print result if the weekday number is 1 
#     print("Yes - today begins with a T")
# # checking the weekday number is equal to 3  using elif conditon  
# elif datetime.datetime.today().weekday() == 3: 
#   # print result if the weekday number is 3   
#   print("Yes - today begins with a T")
# # pass on if the weekday number is not 1 or 3  
# else:
#   # print the day is not beging with T since the weekday is not 1 & 3
#   print("No - today is doesn't begins with T")
