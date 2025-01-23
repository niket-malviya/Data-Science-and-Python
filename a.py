def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Generate a random array of integers
import random
random_array = [random.randint(0, 100) for _ in range(10)]

print("Original array:", random_array)
sorted_array = bubble_sort(random_array.copy())
print("Sorted array (Bubble Sort):", sorted_array)
