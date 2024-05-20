class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # There are 2^n subsets for a set with n elements
        for i in range(1 << n):
            subset_xor = 0
            for j in range(n):
                # If j-th bit of i is set, include nums[j] in subset
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        
        return total_sum
