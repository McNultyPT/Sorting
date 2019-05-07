# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    left_index = 0
    right_index = 0
    arr_index = 0
    
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            merged_arr[arr_index] = arrA[left_index]
            left_index += 1
        else:
            merged_arr[arr_index] = arrB[right_index]
            right_index += 1
        arr_index += 1

    while left_index < len(arrA):
        merged_arr[arr_index] = arrA[left_index]
        left_index += 1
        arr_index += 1

    while right_index < len(arrB):
        merged_arr[arr_index] = arrB[right_index]
        right_index += 1
        arr_index += 1

    return merged_arr

a = [7, 3, 9, 2]
b = [8, 4, 6]

print(merge(a, b))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if arr == []:
        return arr
    elif len(arr) > 1:
        left = merge_sort(arr[:int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)
    return arr

c = [8, 2, 1, 9, 4, 6, 3, 7, 5]

print(merge_sort(a))
print(merge_sort(b))
print(merge_sort(c))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
