def bubble_sort(array, n):
    print(f'Unsorted Array: {array}')
    # we have to run a loop for to execute the passes 
    for i in range(1, n):
        # setting up the pointer 
        ptr = 0
        while ptr <= n-i:
            if ptr == n-i:
                break
            if array[ptr] > array[ptr+1]:
                array[ptr], array[ptr+1] = array[ptr+1], array[ptr]
            ptr = ptr + 1
    return f'Sorted Array: {array}'

array = [
    91,4,7
]
print(bubble_sort(array, len(array)))

# TIME COMPLEXITY 
# f(n) = O(n^2)

# LINEAR_SEARCH 
def linear_search(array, n, item):
    for i in range(n):
        if item == array[i]:
            return i
        else:
            pass
    return None

# print(linear_search([1,2,3,4], len([1,2,3,4]), 4))

# BINARY_SEARCH 
def binary_search(array, n, item):
    beginning = 0
    end = n-1
    mid = int((beginning+end)/2)

    while beginning<=end and array[mid]!=item:
        if item < array[mid]:
            end = mid - 1
        else:
            beginning = mid + 1
        mid = int((beginning+end)/2)
    if array[mid] == item:
        return mid
    else:
        return None

array = [1,2,3,4,5,6]
# print(binary_search(array, len(array), 1))