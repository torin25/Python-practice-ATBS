# collatz sequence
import sys

def collatz(num):
    if num%2==0:
        return num//2
    return 3*num+1

while True:
    try:  
        user_input=int(input("Enter the number: "))
        if user_input<=0:
            print("Please enter natural numbers only")
            continue
        break
    except Exception as e:
        print("Error:",e)
        print(type(e), end='\n')
        print("Invalid input")
        continue
    
    
print("Input: ",user_input)
while True: 
    result=collatz(user_input)
    if result==1:
        print(1)
        break
    print(result)
    user_input=result
    
    

