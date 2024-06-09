class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            if remainder in count:
                res += count[remainder]
            if remainder not in count:
                count[remainder] = 1
            else:
                count[remainder] += 1
        return res


