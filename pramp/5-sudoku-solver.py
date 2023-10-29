"""
  in: board
  out: true / false
    
    Time: O(1) = (9^mxn)
    Space: 
  
    (0,0) (0,3) (0,6)
    012 345 678
    1.. 345 678
    212 345 678
    
    
    (3,0) (3,3) (3,6)
    312 345 678
    412 345 678
    512 345 678
    
    (6,0) (6,3) (6,6)
    612 345 678
    712 345 678
    812 345 678
     
      
    (0,0) (0,2)
    01    23
    1.    ..
    
    (2,0) (2,2) 
    2. ..
    3. ..

    
    https://www.linkedin.com/in/amwadhwani
"""
"""

  board  = 
    [9,1,.,.,7,...],
    [6,.,.,1,9,5,.,.,.]]
    
  
  recur(board):
    if all cells in grid != .
      check if board is valid
    else:
      for i in ints:
        board[r][c] = i 
        recur
   if fully filled do validation check
   if partially filled try all possibilities
    call recursive function for each possibility
    
   
    [.1]
    [32]
  
    [1.]
    [.2]
  
  if cell == .:
    recur
  
   set cell value
   check conditions for *validity* 
    check all cells in row, none == i
    check all cells in col, none == i
    return
    
   
  return: True/False
  
  Brute Approach: 
     For each cell, try all values & check if board is valid
     
     for r in range(rows):
      for c in range(cols):
        ints = [0,1,2,3,4,5,6,7,8,9]
        for i in ints:
          # if cell == .
            board[r][c] = i
     
   
     
     
  
  """
def sudoku_solve():
  pass # your code goes here