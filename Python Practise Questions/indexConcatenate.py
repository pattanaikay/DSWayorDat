"""
list1 = ["m", "na", "i", "pr"]

list2 = ["y", "me", "s", "atik"]

Concatenate this so the output is ["My", "name", "is", "Pratik"]

"""

def concatenateWords(list1:list, list2:list)->list:
    result = [word1 + word2 for word1, word2 in zip(list1, list2)]
    return result

list1 = ["m", "na", "i", "pr"]

list2 = ["y", "me", "s", "atik"]

print(concatenateWords(list1, list2))