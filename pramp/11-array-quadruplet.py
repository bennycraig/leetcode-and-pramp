"""

APPROACH:
Sort the array first
Double for loop for the first two values
Sliding window for the last two values

PSEUDOCODE

https://www.linkedin.com/in/bennycraig/

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
               i        j  l        r
sort arr in logn
n = len(arr)
for i in range(len(arr)):
  for j in range(len(arr)):
    while l < r:
      sum all i,j,l,r
      if sum > target:
        right shift - 1
      if sum <= target:
        left shift + 1
           i=0  l=j+1
        j=i+1   r=n-1
output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
                     u havea sorted arr
                     O(n^2) for two-sum
                     i+j+k+l=target
                     n = sorted arr?
                     n[k]+n[l]=target-(n[i]+n[j]
                     1st sum.   2nd sum
                     
                     
     https://www.youtube.com/watch?v=0K_eZGS5NsU
     interviewing.io
                     
"""

"""
arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
answer = [0,4,7,9]
arr = [0,1,2,3,4,5,7,9]
"""

# [4,4,4,4]
#   i j l r
def find_array_quadruplet(arr, s):
  n = len(arr)
  target = s
  arr.sort()
  for i in range(n):
    for j in range(i+1, n):
      l = j + 1
      r = n - 1
      while l < r:
#        print(arr[i],arr[j],arr[l],arr[r])
        sum = arr[i]+arr[j]+arr[l]+arr[r]
        if sum > target:
          r -= 1
        elif sum < target:
          l += 1
        else: # sum == target
          return [arr[i],arr[j],arr[l],arr[r]]
  return []
  

test = [2, 7, 4, 0, 9, 5, 1, 3]
print(find_array_quadruplet(test,20))
test = [4,4,4,4]
print(find_array_quadruplet(test,16))