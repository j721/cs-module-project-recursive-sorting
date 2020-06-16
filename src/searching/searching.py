# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start +end)//2

    if len(arr) == 0:
        return -1 #empty array
    #if target is equal to the middle index in the array then return it
    if arr[middle] == target:
        return middle
    #if target is less than middle than call recursion and focus on the left side
    #disregard the middle index and those on the right side
    elif arr[middle] > target:
        return binary_search(arr, target, end, middle -1)
    #if target is greater than the middle index than focus on the right side
    #disregard the middle index and those on the left
    else:
        return binary_search(arr, target, start, middle + 1)

 
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# def agnostic_binary_search(arr, target):
    # Your code here

