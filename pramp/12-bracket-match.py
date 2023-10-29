"""
GIVEN: string of brackets
RETURN: minimum number of brackets (to add to input to make correctly matched)

input:  text = “(()”
output: 1
LEFT COUNT: 2
RIGHT COUNT: 1
OUTPUT: L - R

MADE UP 
input:  text = “)(”
LEFT: 1
RIGHT: 1
OUTPUT: 2


“)(())(”
LEFT: 0
RIGHT: 2
SOL: 2


input:  text = “())(”
output: 2
L_STACK: 
R_STACK: )
see right bracket
  if left is 0: add to right
  else: decrement left
see left bracket
  increment left
  
return right + left
###  if r_stack is empty: add to l_stack
###  else: pop from r_stack

input:  text = “()()()()”
L_STACK:  
R_STACK:


input:  text = “(())”
output: 0

https://www.linkedin.com/in/bennycraig/
"""

def bracket_match(text):
  left = 0 
  right = 0
  
  for c in text:
    # see left bracket
    if c == '(':
      left += 1
    # see right bracket
    else: 
      if left == 0:
        right += 1
      else:
        left -= 1
        
  return left + right

# pass # your code goes here
  
  
# TEST CASES
text = "(()" # 1
#text = "(())" # 0
# text = "())(" # 2
print(bracket_match(text))