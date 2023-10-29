"""
 binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]

graph = {
  [0,1]: []
  [0,3]: [[1,3]]
  []
}

visited = [[0,0], [0,1]]
stack = []
islands = 1

for i in len(binaryMatrix) # Rows
  for j in len(binaryMatrix[0]) # Columns 
    if i,j not in visited:
      add i,j to visited
      if binaryMatrix[i,j] == 1:
        add i,j to stack
        islands += 1
        while stack:
          cur = stack.pop()
          # add cur to visited # remove?
          for all neighbors
            if neighbor not in visited:
              if neighbor == 1:
                add neighbor location to stack
              else:
                add neighbor to visited
                
                
  Loop through neighbors
    Check the boundaries
    left = i, j-1
    up = i-1, j
    right = i, j+1
    down = i+1, j
    if left[1] >= 0: # inside
    if up[0] >= 0: 
    if

"""

def get_number_of_islands(binaryMatrix):
  visited = set() # optimized over a list due to lookup time
  stack = [] 
  islands = 0
  
  for i in len(binaryMatrix): # Rows
    for j in len(binaryMatrix[0]): # Columns 
      if (i,j) not in visited:
        print(i,j)
        # visited.add((i,j))
        if binaryMatrix[i,j] == 1:
          stack.append((i,j))
          islands += 1
          while stack:
            cur = stack.pop()
            # if binaryMatrix
            if cur not in visited:
              visited.add((i,j))
              if i >= 0 and i < len(binaryMatrix) and j >= 0 and j < len(binaryMatrix[0]):
                left = (i, j-1)
                up = (i-1, j)
                right = (i, j+1)
                down = (i+1, j)
                neighbors = [left, up, right, down]
                for n in neighbors:
                  if binaryMatrix[n[0], n[1]] == 1:
                    stack.append(n)
                  else: # neighbor is 0, add to visited
                    visited.add(n)
                  
  return islands



"""
def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                islands += 1
                self.visit(grid, i, j, visited)
        return islands
        
  def visit(self, grid, i, j, visited):
      coord = (i, j)
      if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or coord in visited or grid[i][j] == "0":
          return
      visited.add(coord)
      self.visit(grid, i + 1, j, visited)
      self.visit(grid, i, j + 1, visited)
      self.visit(grid, i - 1, j, visited)
      self.visit(grid, i, j - 1, visited)
            
        
  
#binaryMatrix = [ [0,    1,    0,    1,    0],
 #                [0,    0,    1,    1,    1],
  #               [1,    0,    0,    1,    0],
   #              [0,    1,    1,    0,    0],
    #             [1,    0,    1,    0,    1] ]

#get_number_of_islands(binaryMatrix)
"""