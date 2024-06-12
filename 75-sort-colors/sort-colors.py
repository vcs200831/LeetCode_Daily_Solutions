class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        m = 0
        
        def swap(m,j):
            t = nums[m]
            nums[m] = nums[j]
            nums[j] = t
        
        
        while m<=r:
            if nums[m] == 0:
                swap(l,m)
                l +=1
                m +=1
            elif nums[m] == 2:
                swap(m,r)
                r-=1
            else:
                m +=1
                
                 
        