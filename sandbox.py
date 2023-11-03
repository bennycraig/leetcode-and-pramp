"""
THIS PROGRAM IS FOR TESTING IDEAS QUICKLY
"""

if __name__ == "__main__":
  
  # ENUMERATE
  # myString = "HELLO"
  # for index, c in enumerate(myString):
  #   print(index, c)

  # CONVERT LIST TO SET
  # numList = [1,2,3,4]
  # numSet = set(numList)
  # for num in numSet:
  #   print(num)

  # NAVIGATING LIST BACKWARDS & FORWARDS
  numList = [1,2,3,4]
  
  # FORWARDS
  for i in range(0, len(numList), 1): 
    print(i) # prints 0123
  
  # BACKWARDS
  for i in range(len(numList)-1, -1, -1): 
    print(i) # prints 3210

