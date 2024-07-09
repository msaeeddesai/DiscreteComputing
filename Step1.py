# # Initialize the array
# arr = [64, 34, 25, 12, 22, 11, 90]

# # Initialize variables
# n = len(arr)
# i = 0

# # Start the outer loop
# while i < n:
#     swapped = False
#     j = 0
    
#     # Start the inner loop
#     while j < n-i-1:
#         # Swap if the element found is greater than the next element
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#             swapped = True
#         j += 1
    
#     # If no two elements were swapped by the inner loop, then the list is sorted
#     if not swapped:
#         break
    
#     i += 1

# # Print the sorted array
# print("Sorted array:", arr)


# PRAM Model 1

import threading

# Function to perform parallel comparison and swap
def compare_and_swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

# Parallel Bubble Sort using PRAM model
def parallel_bubble_sort(arr):
    n = len(arr)
    # Create a list of threads
    threads = []
    for i in range(n):
        # Parallelize the inner loop
        for j in range(0, n-i-1):
            t = threading.Thread(target=compare_and_swap, args=(arr, j, j+1))
            threads.append(t)
            t.start()
        # Wait for all threads to complete
        for t in threads:
            t.join()
        threads = []

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
parallel_bubble_sort(arr)
print("Sorted array:", arr)


