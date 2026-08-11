class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        num_set = set(nums)
        for n in range(0,n+1):
            if n not in num_set:
                return n
        return None
           

       
        