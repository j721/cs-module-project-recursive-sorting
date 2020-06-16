# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    #initialize array a and array b to zero
    a = 0
    b = 0

    #iterate through the length of both arrays a and b combined
    for i in range(0, elements):
        #compare a and b
        #if a is out of range, push into b array and iterate
        if a>= len(arrA):
            merged_arr[i] = arrB[b]
            b+=1
        #if b is out of range, push into array and iterate through array a   
        elif b>= len(arrB):
            merged_arr[i] =arrA[a]
            a +=1
        #if a element at arrA index is smaller, than put into merged array and iterate both
        elif arrA[a] < arrB[b]:
            #add the lower arrA[a] into the merged arr
            merged_arr[i] = arrA[a]
            a+=1
        #if b element at arrB is smaller than put into merged array and iterate both   
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

