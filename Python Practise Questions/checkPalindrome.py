"""
Given a list of integers, write a function to check if it's a palindrome.

"""

def isPalindrome(numList):
    return numList == numList[::-1]

# Example usage
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

print(list1, "is palindrome:", isPalindrome(list1))  
print(list2, "is palindrome:", isPalindrome(list2))  