# Author : Babu Baskaran 
# Date   : 05/04/2019 Time : 19:00 pm
# Solution for problem number 1
user1=int (input("Please Enter a Positive Integer : "))

start = user1

i = 1

ans = 1
while i<= start:
    ans = ans+i
    i = i + 1
    
print(ans)