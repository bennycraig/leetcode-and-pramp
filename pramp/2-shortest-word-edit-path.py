def isStep(current_word, word):
  """
  Finding all steps in words:
  Loop through words w
    different chars = 0
    Loop through all chars in current_word and all chars word:
      if current_word[i] != word[w][i] 
        diff_chars += 1
    if diff_chars == 1:
      return True
  """
  #if len(current_word) != len(word):
   # return False
  
  #diff_chars = 0
  #for c in len(current_word):
    # How to compare words of different length
   # print(current_word[c], word[c])
    #if current_word[c] != word[c]
     # diff_chars += 1
      
#  if diff_chars == 1:
 #   return True
  #return False

def shortestWordEditPath(source, target, words):

  stack = []
  current_word = source
  dist = 0
  
  # Add initial steps
  for w in words:
    if isStep(current_word, w):
      stack.appennd(w, dist) # Add word and distance
      
      # Delete word from words
      
  # Pop from end of list
  current_word, dist = stack.pop()
      
  while len(stack) != 0: 
    if current_word == target:
      return dist
    
    for w in words:
      # if isStep(current_word, w):
      
      if len(current_word) != len(word):
        continue
  
    # Count num diff chars
    diff_chars = 0
    for c in len(current_word):
      print(current_word[c], word[c])
      if current_word[c] != word[c]:
        diff_chars += 1

    if diff_chars == 1:
      stack.appennd(w, dist + 1) # Add word and distance
      # Delete the wth element from words
      words.pop(w)
    else:
      continue
      
        
        
    current_word, dist = stack.pop()
    
    
    
    
      
	
  

