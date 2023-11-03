#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

"""
Given an unsorted array of integer nums, return the 
LENGTH OF THE LONGEST CONSECUTIVE ELEMENTS SEQUENCE

APPROACH: From Neetcode
- Convert the list into a set
longest_sequence = 0 
- Loop through each num in set
    - Check for left neighbor & then find length of sequence
    - If no left neighbor (prefix), it's beginning of range
        - sequence_length = 1 
        - curr_num = num
        WHILE LOOP:
        - If right neighbor is in set, increase sequence length and check
            - Increase sequence length
            - Compare with longest_sequence 
            - update curr_num += 1
    - If left neighbor is in set, not beginning of range (continue)
"""

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_seq = 0
        for num in numSet:
            # If no left neighbor, beginning of range
            if (num - 1) not in numSet:
                seq_length = 1
                cur = num
                
                if longest_seq < seq_length: # update max seq length if needed
                    longest_seq = seq_length
                
                # While there is a right neighbor
                while ((cur + 1) in numSet):
                    seq_length += 1
                    cur += 1
                    if longest_seq < seq_length:
                        longest_seq = seq_length
        return longest_seq
                
            

        
        
# @lc code=end

