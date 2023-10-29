"""
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

word = "makes"
words = ['perfect']

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
          
      approach 1: 
      
      join the chars into strings (stopping at each space)
      append the strings to a list
      iterate through the list in reverse 
      add chars one by one to an output list
      
      approach 2: 
      loop through input array in reverse
      when a space is encountered start a forward loop until end of word
"""

def reverse_words(arr): 
  output = []
  
  #join the chars into strings (stopping at each space)
  words = []
  word = ""
  for char in arr:
    if char != " ":
      word += char
    else: 
      words.append(word)
      word = ""
  words.append(word) # last word appended to list
      
  #append the strings to a list
  #iterate through the list in reverse 
  for w in range(len(words) - 1, -1, -1): # TODO: check syntax! try different index
    for char in words[w]:
      output.append(char)
    # DO NOT APPEND SPACE ON LAST WORD
    output.append(' ')
  output.pop()
  
  #add chars one by one to an output list
  return output

# interviewing.io