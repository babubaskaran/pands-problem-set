# Author : Babu Baskaran 
# Date   : 07/04/2019 Time : 17:00 pm
# Solution for problem number 4
# Version 1.0

# define the function col to perform the repeated steps based on condition
def col(user1):
    # if condition to check the entered value is divide by 2 print it
    if user1 % 2==0:
     #print the result 
     print (int(user1/2))
     # return to value of function 
     return user1/2
    # elif condition to check next value is odd 
    elif user1 % 2==1:
      # perform  multiply by 3 and add one  
      user2 = (3*user1+1)
      # print the result
      print (int(user2))
      #  return to value of function
      return user2
# getting user input 
n = input("Please Enter a Positive Integer : ")
# while condition to check next value is not equal to 1
while n !=1:
  # asssigning value of n from the function
  n = col(int(n))