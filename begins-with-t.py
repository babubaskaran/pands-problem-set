# Author : Babu Baskaran 
# Date   : 05/04/2019 Time : 19:00 pm
# Solution for problem number 2
# Version 1.0
# import the datetime of the system using import syntax
import datetime
# checking the weekday number is equal to 1 using if condition
if datetime.datetime.today().weekday() == 1: 
    # print result if the weekday number is 1 
    print("Yes - today begins with a T")
# checking the weekday number is equal to 3  using elif conditon  
elif datetime.datetime.today().weekday() == 3: 
  # print result if the weekday number is 3   
  print("Yes - today begins with a T")
# pass on if the weekday number is not 1 or 3  
else:
  # print the day is not beging with T since the weekday is not 1 & 3
  print("No - today is doesn't begins with T")