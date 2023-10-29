"""
GIVEN: arr
OUTPUT: sorted array (using flip function)

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output

INPUT: [2,1]

Whenever the right element > left elt, flip k elements



INPUT : [3,5,2,4] flip 2

[5,3,2,4] flip 4
[4,2,3,5] flip 3
[3,2,4,5] flip 2
[2,3,4,5]
 

[5],[3,2,4] flip(arr,k=2)
[5],[2,3,4] flip 3
[5],[4,3,2]

[1,3,2] flip first 2
[2,3,1] flip 3
[3,2,1] flip 2
[1,2,3] flip 3

INPUT: [3,1,2]
[2,1,3]
[1,2,3]

SORT PSEUDOCODE:
n = len(arr)
Find index of max elt 
if max not at end:
  if max not at beginning:
    flip(arr, maxidx) # places at beginning
  flip(arr, n-1)
  decrement n
  
Place max elt at beginning (by flipping up to index)
Flip entire array (max will be at end)

FLIP PSEUDOCODE:
Set left pointer 
while left < k:
  swap left and k
  increment left and decrement k

max
min

arr[::-1]
arr[:max + 1] = arr[:max+1][-1]

"""
def find_max(arr):
  #Find index of max elt 
  max = arr[0]
  max_idx = 0
  for i in range(n):
    if arr[i] > max:
      max = arr[i]
      max_idx = i
      
  print(max, max_idx)
  return max_idx

def pancake_sort(arr):
  n = len(arr)
  if n == 0:
    return []
  
  # loop until n = 1
  while n > 1:    
    max_idx = find_max(arr[0:n-1])
    #if max not at end:
    if max_idx != n - 1:
     # if max not at beginning:
      if max_idx != 0:
        flip(arr, max_idx) # places at beginning
    flip(arr, n-1)
   # decrement n
    n -= 1
    
  return arr

def flip(arr, k):
  left = 0
  while left < k:
    arr[left], arr[k] = arr[k], arr[left]
    left += 1
    k -= 1
  
  return arr
  # TODO: returns index? 

  
test = [2,1]
test = [2,1,3]
test = []
test = [2,1,3,4]
output = pancake_sort(test)
print(output)
  
# TIME: O(n^2)
# no sorting arrays in O(n) time!
# SPACE
  
  
  
  
  
  
  
  