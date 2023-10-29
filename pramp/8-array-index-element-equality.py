"""input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
"""
"""
Brute force:
loop through array
  if index equals value, return val
else return -1
solution 1:
  for i in range(len(arr)):
    print(i, arr[i])
    if i == arr[i]:
      return i
  return -1
  
  [5,6]
  [5,6,7]
  [0] 
  half = 1/2 = 0 (floor)

"""
import math
def index_equals_value_search(arr):
  start = 0
  end = len(arr)
  half = int(math.floor(len(arr) / 2))
  print(half)

  
  while start < len(arr):
    i = int(math.floor(start + end) / 2)
    if arr[i] - i < 0:
      start = i+1
    elif (arr[i] - i == 0) and ((i == 0) or (arr[i-1] - (i-1) < 0)):
      return i
    else:
      end = i-1

  return -1
      
      
#  for i in range(half):
 #   if i == arr[i]:
  #    return i
#  second_half = arr[half:]
 # index_equals_value_search(second_half)
