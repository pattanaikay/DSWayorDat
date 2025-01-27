"""
Given an integer, check if it is an Armstrong number or not.

"""

def isArmstrongNumber(num:int)-> bool:
    
    armNumSum = 0
    n = len(str(num))
    originalNum = num

    while num > 0:
        temp = num % 10
        armNumSum += temp ** n 
        num //= 10

    return armNumSum == originalNum
        
number = 1530        
armstrongNumberCheck = isArmstrongNumber(number)
if armstrongNumberCheck:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")