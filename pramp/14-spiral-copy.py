"""
GIVEN: 2d array of ints
RETURN: array traversing the input in clockwise spira


input: inputMatrix = [[1,2]]

input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

APPROACH:
first_r, first_c = 0,0
last_r, last_c = len(inputMatrix) - 1, len(inputMatrix[0]) - 1
result = []

while (first_r <= last_r and first_c <= last_c):
  first pass forward row (starting at first_c : last_c)
    append elt
  increment first_r
  traverse last col in ascending order (first_r : last_r)
  decrement last_c
  traverse last row in descending row (last_c : first_c)
  decrement last_r
  traverse first col in descedning order (last_r : first_r)
  increment first_c

return result 


inputMatrix = [[1,2]]
first_r = 1
first_c = 0 
last_r = 0
last_c = 0

"""

def spiral_copy(inputMatrix):

  first_r, first_c = 0,0
  last_r, last_c = len(inputMatrix) - 1, len(inputMatrix[0]) - 1
  result = []

  while (first_r <= last_r and first_c <= last_c):
    # first pass forward row (starting at first_c : last_c)
    for i in range(first_c, last_c + 1, +1):
      result.append(inputMatrix[first_r][i])
    # increment first_r
    first_r += 1
    
    # traverse last col in ascending order (first_r : last_r)
    for i in range(first_r, last_r + 1, +1):
      result.append(inputMatrix[i][last_c])
    last_c -= 1 # decrement last_c
    
    # traverse last row in descending row (last_c : first_c)
    if first_r <= last_r:
      for i in range(last_c, first_c - 1, -1):
        result.append(inputMatrix[last_r][i])
      last_r -= 1 # decrement last_r
    
    # traverse first col in descedning order (last_r : first_r)
    if first_c <= last_c:
      for i in range(last_r, first_r - 1, -1):
        result.append(inputMatrix[i][first_c])
      first_c += 1 # increment first_c

  print(result)
  return result 

inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

spiral_copy(inputMatrix)