# Author : Babu Baskaran 
# Date   : 06/04/2019 Time : 21:00 pm
# Solution for problem number 4
# Version 1.0
user1=int (input("Please Enter a Positive Integer : "))

def col(user1):
  while user1 !=1:

    if user1 % 2==0:
      user1 = (user1/2)
      return print (int(user1))
    elif user1 % 2==1:
      user1 = (3*user1+1)
      return print (int(user1))  
      
col(user1)