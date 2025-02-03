from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1
        inc_length = 1
        dec_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc_length += 1
                dec_length = 1  # Reset decreasing length
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec_length += 1
                inc_length = 1  # Reset increasing length
            else:  # Reset both if equal
                inc_length = 1
                dec_length = 1
            
            max_length = max(max_length, inc_length, dec_length)
        
        return max_length