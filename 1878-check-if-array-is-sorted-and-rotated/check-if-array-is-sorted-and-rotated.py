from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Circular check
                count += 1
        
        return count <= 1  # Only one break allowed