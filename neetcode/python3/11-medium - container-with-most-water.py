#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

"""
BRUTE FORCE:
- O(n^2): Try out all possible pairs
    - Find min height value
    - Area = min height x difference in indices
- Keep track of max area
"""

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        BRUTE FORCE: Written by me
        """
        # max = 0
        # for i1, h1 in enumerate(height): # index1 & height1
        #     for i2, h2 in enumerate(height): # index2 & height2

        #         if i2 <= i1: # inner loop should always start after
        #             pass
        #         base = i2 - i1
        #         minHeight = h1 if h1 < h2 else h2 # ternary syntax
        #         area = base * minHeight
        #         if max < area:
        #             max = area
        # return max
    
        """
        BRUTE FORCE: From Neetcode
        - Range-based for loops are cleaner when using indices
            - REMEMBER: _stop parameter is exclusive -> Go until len(height) to get to end of list
        - The min() and max() functions are SUPER clean -> use them when you can!
        """
        # result = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r-l) * min(height[l], height[r])
        #         result = max(result, area)
        # return result
    
        """
        OPTIMIZED APPROACH:
        - Start with left and right pointers at end
        - Figure out current area
            area = (r-l) * min(height[l], height[r])
        - Move the pointer with the lower height inwards 
            (moving the max height pointer could not increase the area)
        - Keep track of maxArea
        """
        # initialize pointers
        l, r = 0, len(height)-1

        # compute first area
        area = (r-l) * min(height[l], height[r])
        maxArea = area

        while (l < r):
            if height[l] < height[r]:
                l+=1
            else: 
                r-=1 # note: if heights are same, you can move either
            area = (r-l) * min(height[l], height[r])
            maxArea = max(area, maxArea)

        return maxArea




                

        
# @lc code=end

