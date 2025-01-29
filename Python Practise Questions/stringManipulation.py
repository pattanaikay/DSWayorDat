"""
Problem: Write a function that takes a list of strings and returns a new list containing
only the strings that:
- Start with a vowel
- Have length greater than 4
- Convert the matching strings to uppercase

Example:
Input: ['apple', 'banana', 'elephant', 'ice', 'orange']
Expected Output: ['APPLE', 'ELEPHANT', 'ORANGE']
"""

def stringManipulation(word_list:list)->list:
    final_word_list = []
    for word in word_list:
        if word.startswith(('a', 'e', 'i', 'o', 'u')) and len(word)>4:
            final_word_list.append(word.upper())
            
    return final_word_list

wordlistsample = ['apple', 'banana', 'elephant', 'ice', 'orange']

print(stringManipulation(wordlistsample))