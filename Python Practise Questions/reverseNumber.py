"""
Given an integer, reverse it. 

"""

def reverseNum(num:int)-> int:
    revNum = 0
    
    while num > 0:
        temp = num % 10
        revNum = (revNum*10) + temp
        num = num // 10
    
    return revNum

reversedNum = reverseNum(643)
print(f"The reverse of the number 643 is {reversedNum}")