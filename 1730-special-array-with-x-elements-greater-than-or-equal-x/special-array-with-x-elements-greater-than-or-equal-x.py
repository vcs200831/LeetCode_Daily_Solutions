class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return -1

