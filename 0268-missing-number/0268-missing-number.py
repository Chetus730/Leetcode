class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        for n in range(0,n+1):
            if n not in nums:
                return n
        return None
           

       
        