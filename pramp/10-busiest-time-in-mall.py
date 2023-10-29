"""
Busiest moment at mall last year

arr of size 3
[timestamp, count visitors, exit/entrance]

Only look at entrances (1)
Only look at range in last year

max_visitors = 0
max_timestamp = ?
timestamp = ..9425
visitors = 0 
                                        visitors
                                        0
data =          [ [1487799425, 14, 1],  14
                 [1487799425, 4,  0],   10  
                 [1487799425, 2,  0],   8
                                        
                                        0
                 [1487800378, 10, 1],   10
                 
                                        0
                 [1487801478, 18, 0],   -18
                 [1487801478, 18, 1],   0
                 
                 [1487901013, 1,  0],   1
                 [1487901211, 7,  1],   8
                 [1487901211, 7,  0] ]  1
                                      visitors
                                      0
                 [[1487799425,21,0],  -21
                                      
                                      0
                 [1487799427,22,1],   22
                 [1487901318,7,0]]

                 
"""
def find_busiest_period(data):
  
  max_visitors = 0 # change this to negative inf (or set in the loop)
  timestamp = data[0][0]
  max_timestamp = data[0][0]
  visitors = 0 
  # day = 
  
  for d in range(len(data) - 1):
    # Check for new timestamp, new timestamp rep. final visitor count
    if data[d][0] != timestamp:
      if visitors > max_visitors:
        max_visitors = visitors
        max_timestamp = timestamp
      # visitors = 0
      timestamp = data[d][0]
    # Increment/decrement visitors
    if data[d][2] == 1: # entrance
      visitors += data[d][1]
    else: 
      visitors -= data[d][1]
  
  if visitors > max_visitors:
    max_visitors = visitors
    max_timestamp = timestamp
  
  return max_timestamp
      

"""
APPROACH:
Keep track of changes of timestamp
Count visitors for each timestamp
  Increment when data[2] == 1, else decrement 
Keep track of max visitors
  
"""
