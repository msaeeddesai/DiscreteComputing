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



