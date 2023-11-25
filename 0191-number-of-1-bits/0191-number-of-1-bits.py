class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            rem = n % 2 
            if rem == 1:
                count+=1
            n = n >> 1 
        """
        while n:
            n = n & (n-1)
            count+=1
        """ 
        return count

s1 = Solution()
res = s1.hammingWeight(0b00000000000000000000000000001011)
print(res)
res=s1.hammingWeight(0b00000000000000000000000010000000)
print(res)
res = s1.hammingWeight(0b11111111111111111111111111111101)
print(res)
        
        