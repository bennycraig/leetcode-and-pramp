"""
INPUT: shiftArr
RETURN: index of num in shiftArr (or -1)

APPROACH:
Find the cut off point - O(log n)
Modified binary search - O(log n)

PSEUDO CODE: 
Set min to first elt
Binary search for elt < min && elt to left must be greater
Found cut off point (could be start of array)
Choose leftArr or rightArr to search
Binary search for num in one side 
"""
def shifted_arr_search(shiftArr, num):
    #Set min to first elt
    min = shiftArr[0]

    #Binary search for elt < min && elt to left must be greater
    # Set start and end
    start = 0
    end = len(shiftArr)

    while start < end:
        # if elt < min, search left
        half = (start + end) // 2
        if shiftArr[half] < shiftArr[end]:
            end = half
            min = shiftArr[half]

        # else, search right
        else: 
            start = half
    
    return min
    
shiftArr = [9, 12, 17, 2, 4, 5]
num = 2
print(shifted_arr_search(shiftArr, num))

#Found cut off point (could be start of array)
#Choose leftArr or rightArr to search
#Binary search for num in one side 

"""
EXAMPLE 
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left
Two sorted arrays
LeftArr = [9, 12, 17]
RightArr = [2, 4, 5]

Normal Binary: n
Find smallest bin search: n where n < min and val to left is greater

output: 3 # since it’s the index of 2 in arr


Offset: number of shifts (any val 0 to arr.length -1)


"""