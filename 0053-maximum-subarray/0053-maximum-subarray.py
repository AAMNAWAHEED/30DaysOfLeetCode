class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = 0
        curmax = nums[0]
        for n in nums:
            if maxsum < 0:  #if getting total -nagetive value igonre it
                maxsum=0
            maxsum+=n
            curmax = max(curmax,maxsum)
        return curmax
s1 = Solution()
res = s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)