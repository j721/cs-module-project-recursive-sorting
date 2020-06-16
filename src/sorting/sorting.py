# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    #pointers a for arrA and b for ArrB start at 0
    a = 0
    b = 0

    #iterate through the length of both arrays a and b combined
    for i in range(0, elements):
        #compare a and b
        #if a pointer is out of range (greater or equal to arrA length)
        # push into b array and iterate
        if a>= len(arrA):
            merged_arr[i] = arrB[b]
            b+=1
        #if b pointer is out of range(greater/equal to arrB length)
        # push into a array and iterate through array a   
        elif b>= len(arrB):
            merged_arr[i] =arrA[a]
            a +=1
        #if a element at arrA index is smaller, than put into merged array and iterate through both
        elif arrA[a] < arrB[b]:
            #add the lower arrA[a] into the merged arr
            merged_arr[i] = arrA[a]
            a+=1
        #if b element at arrB index is smaller than put into merged array and iterate through both 
        else:
            merged_arr[i] =arrB[b]
            b +=1  
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    #merge_sort does the splitting of the arrays into halves 
    #base condition
    #if array size >1
    if len(arr) >1:
        #find the middle of arr
        #sort stuff in the left side and put stuff to the left in left side
                         #from the beginning to the half way point
        left = merge_sort(arr[0:len(arr)//2 ])
        #sort stuff in the right side and put stuff to the right in right side
                                 #from the halfway point to the end
        right = merge_sort(arr [len(arr)//2:])

        #merge left and right
        arr = merge(left,right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

