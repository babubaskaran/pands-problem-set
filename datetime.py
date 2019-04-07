# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 22:55 pm
# Solution for problem number 8
# Version 1.0
# import the datetime of the system using import syntax
#import time 

import time 
day=time.strftime(%d)  
if 4 <= day <=20 or 24 <= day <= 30:
    suffix = "th"
else:
    suffix = ["st","nd"][day%10-1]
b = time.strftime("%A, %B %d",suffix, "%Y at %I:%M%p")
print(b)

