"""
Sorts the given array in ascending order using the bubble sort algorithm.

"""

def numBubblesort(arr:list) -> list:
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted Array:", data)

sorted_data = numBubblesort(data)
print("Sorted Array:", sorted_data)