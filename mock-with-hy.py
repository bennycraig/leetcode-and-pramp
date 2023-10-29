"""
NOTES FROM INTERVIEW;
- err on side of starting code sooner
- try to get to a non-optimal solution faster
- 31 minutes part 1 
- 20 mintes part 2

Outliers 

need to be able to remove numbers given to me
remove all occurrences of a given value 
recalculating the mode:
  if num removed is the mode
    loop through frequencies dictionary and find mode


START: 12:09

Create a class 
- take in numbers (scalar)
- keep in memory to look at
- summarize data into stats
  - sum of all values
  - mode of all values
  - get distinct numbers 
    - add numbers 1,1,2,3
    - 

ADD NUMBERS
  Keep track of sum
  Add value to a dictionary (key= number, value= frequency)
  Keep track of mode (highest frequency)
    Add numbers to mode when max frequency encountered
    Remove numbers from list when higher frequency encountered

GET SUM
  Return the sum

GET MODE
  Return the mode

GET DISTINCT NUMBERS
  Print all items in dict



"""

class AmazonNums():
  sum = 0
  highest_freq = 0
  mode = []
  frequencies = dict() # FIXME: NAMING CONVENTION: 'numByFrequency' (something-by-something)

  def addNum(self, num):
    # Keep track of sum
    self.sum += num
    # Add value to a dictionary (key= number, value= frequency)
    if num in self.frequencies:
      self.frequencies[num] += 1
    else:
      self.frequencies[num] = 1


    # Keep track of mode (highest frequency)
    if self.frequencies[num] == self.highest_freq:
      self.mode.append(num)
      # self.highest_freq = self.frequencies[num]

    elif self.frequencies[num] > self.highest_freq:
      self.mode.clear()
      self.mode.append(num)
      self.highest_freq = self.frequencies[num]

  def getSum(self):
    return self.sum
  
  def getMode(self):
    return self.mode
  
  def getDistinct(self):
    return self.frequencies.keys() # returns only keys
  
  def removeNum(self, num):
    # decrement sum
    for i in range(self.frequencies[num]):
      self.sum -= num # FIXME: MAKE THIS EASIER TO READ

    # remove all occurrences of a given value 
    del self.frequencies[num]

    # recalculating the mode:
    if num in self.mode:
      self.mode.remove(num)
    
    if len(self.mode) == 0:
      self.highest_freq = 0
      for num, freq in self.frequencies.items(): # FIXME: WRITE THIS CODE AS ITS OWN FUNCTION TO AVOID DUPLICATION
        if freq == self.highest_freq:
          self.mode.append(num)

        elif freq > self.highest_freq:
          self.mode.clear()
          self.mode.append(num)
          self.highest_freq = freq


    #   if num removed is the mode
    #     loop through frequencies dictionary and find mode

  
"""
[] 
SUM 0
MODE None
DISTINCT []

[1,2,3]
SUM 1
MODE [1,2,3]
DISTINCT [1,2,3]


"""
nums = [1,2,3,3]    
# nums = []
test = AmazonNums()
for num in nums:
  test.addNum(num)

print(test.getMode()) # 3
print(test.getSum()) # 9
print(test.getDistinct()) 
test.removeNum(3)
print(test.getMode()) # 1,2
print(test.getSum()) # 3
print(test.getDistinct()) # 1,2
      
  

    
