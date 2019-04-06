# Author : Babu Baskaran 
# Date   : 05/04/2019 Time : 19:00 pm
# Solution for problem number 2
# Version 1.0

import datetime

if datetime.datetime.today().weekday() == 1:  
    print("Yes - today begins with a T")
elif datetime.datetime.today().weekday() == 3:    
  print("Yes - today begins with a T")
else:
  print("No - today is doesn't begins with T")