def shortestCellPath(grid, sr, sc, tr, tc):
  visited = [] 
  queue = [] 
  r = sr
  c = sc
  d = 0
  queue.append((r,c,d))
  
  # If the queue is empty, stop
  while len(queue) > 0 :
    
    # Update current location 
    r,c,d = queue.pop(0)
    
    # check if r,c is in visited
    if (r,c) in visited:
        continue
    # if not then add it to visited
    # if in visited skip eeverything below
    visited.append((r,c))
    
# https://www.linkedin.com/in/bennycraig/
    
    # Check boundaries
    width = len(grid[0])
    height = len(grid)

    # Check each location 
    if c-1 >= 0 and grid[r][c-1] == 1:
      queue.append((r,c-1,d+1))
    if r-1 >= 0 and grid[r-1][c] == 1:
      queue.append((r-1,c,d+1))
    if c+1 < width and grid[r][c+1] == 1:
      queue.append((r,c+1,d+1))
    if r+1 < height and grid[r+1][c] == 1:
      queue.append((r+1,c,d+1))

    # Check if in target loc
    if r == tr and c == tc:
      return d
    
  return -1

# BFS 
# start = [sr][sc]
# end = [tr][tc]

# Find all possibilities of movement from start
# Check all grid location (left, right, up, down)
# If traversable

# Queue
# Keep track of locations visited 

# Visit location from the queue (pop the queue)
  

# Keep track of length of the path 

# (0,3, 0), (0,2, 1) (1,3,1), (0,1, 2)

# 1 1 1 1
# 0 0 0 1
# 1 1 1 1


# Check if outside of the range of the grid