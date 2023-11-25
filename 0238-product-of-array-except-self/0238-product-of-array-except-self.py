class Solution:
    def productExceptSelf(self, nums):
        """
        answer = []
        for i in range(len(nums)):
            ans =1
            for index in range(len(nums)):
                if index != i:
                    ans = nums[index] * ans     
            answer.append(ans)
        return answer
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
            
s1 = Solution()
print(s1.productExceptSelf([1,2,3,4]))
print(s1.productExceptSelf([-1,1,0,-3,3]))

        