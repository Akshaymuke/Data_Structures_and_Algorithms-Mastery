# Problem link - https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/description/
# Approach:
# The problem treats one array (lets say nums1) as a circular loop. 
# The goal is to see which "shift" or "rotation" of this loop aligns the most elements with the second array (nums2).
# Iterate through all possible shifts:Since the array has a length n, there are exactly n possible cyclic shifts (from 0 to n-1).
# Calculate the new position:For each shift, the algorithm calculates where an element originally at index pos would end up after being shifted by num_of_shift. 
# This is done using the modulo operator:new_pos = (pos + num_of_shift) mod n.
# Count Matches:At every shift, it compares nums1[new_pos] with nums2[pos]. 
# If they are equal, its a "match.
# "Track the Maximum:A global variable max_cnt keeps track of the highest number of matches found across all $n$ shifts.
             
# Time Complexity: O(n2)
# Space Complexity: O(1)

class Solution:
    def maximumMatchingIndices(self, nums1, nums2):
        n = len(nums1)
        max_cnt = 0
        for num_of_shift in range(n):
            curr_cnt = 0
            for pos in range(n):                        
                new_pos = (pos + num_of_shift) % n          # logic of shifting by ith position
                if nums1[new_pos] == nums2[pos]:
                    curr_cnt += 1
            max_cnt = max(max_cnt,curr_cnt)
        return max_cnt