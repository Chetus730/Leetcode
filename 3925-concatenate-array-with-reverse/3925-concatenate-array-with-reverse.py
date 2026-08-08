class Solution(object):
    def concatWithReverse(self, nums):
        # return nums+nums[::-1]
        i=len(nums)-1
        count=[]
        while i>=0:
            count.append(nums[i])
            i-=1
        return nums+count



   
        