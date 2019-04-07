# Author : Babu Baskaran 
# Date   : 05/04/2019 Time : 17:00 pm
# Solution for problem number 1
# taking user input 
user1=int (input("Please Enter a Positive Integer : "))
# assigning user input into a variable
start = user1
# set i start value into 1
i = 1
# set value of variable ans to zero
ans = 0
# check the i value is equal or less than variable start
while i<= start:
    # increase the value of variable ans by 1
    ans = ans+i
    # increase the value of i by 1
    i = i + 1
# print the output sum of integer to the user    
print(ans)