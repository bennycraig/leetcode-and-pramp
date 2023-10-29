def get_shortest_unique_substring(arr, str):
  pass # your code goes here

# https://umich.zoom.us/j/7365690313 
  """
  As soon as substring with len() == len(arr), return this string 

  matches which are longer then len(arr):


  Brute: find all substrings which contain all chars, return the shortest

  Keep the length of the window at MOST == len(shortest)


  arr = ['x', 'y', 'z'] str = "xaaaaaayz"
    arr = ['x', 'y', 'z'] str = "xaaaaxaayz"

arr = ['x','y','z'], str = "xyyzyzyx"
  
  # Only add chars from arr into map
  index_map = { 
  x:0
  y:7
  z:8
  }
  # Check whether each char is in arr
  count_map = {
  x:1
  y:1
  z:1
  }
  

    # Check which chars in arr are in the window -> separate map?

  l = 0
  r = 0
  char_count = dict() # initialize all chars from arr to equal 0
  substrings = [] # contains all matching substrings
  
  while r < len(str):
    

    
    # Loop through all chars between l & r
      # Are all chars from arr in substring?
      Add all chars in arr to char_count
      
     
    # Check if all char_counts == 1 # match
      substring = str[l:r]
      match = substring
      Can you hear me  one second



    # if not, increment r
    
    When we see a char in arr, increment l
    # If we have a substring match, l++
    If 
  
  # Can stop incrementing l, when substring is not match
  while l < len(str)
    
      
  Find shortest substring and return


  """

  shortest_substring = str # How will I first initialize the shortest string?
  shortest = len(shortest_substring)
  
  min_len = len(arr)
  l = 0 
  r = 0
  
    for c in range():
  