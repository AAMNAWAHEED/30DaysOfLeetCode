class Solution:
    def maxProfit(self, prices):
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r+=1
        return maxP
        """
        buy_stock_value = min(prices)
        buy_index = prices.index(buy_stock_value)
        if buy_index == len(prices) - 1:
            return 0
            #return "in this case,no transactions are done and the max profit = 0"
        else:
            index = buy_index +1
            maximum = prices[index]
            index+=1
            while index <len(prices):
                if maximum < prices[index]:
                    maximum = prices[index]
                index+=1
            profit = maximum - buy_stock_value
            return profit
        """
s1 = Solution()
output = s1.maxProfit([7,1,5,3,6,4])
print(output)
output = s1.maxProfit([7,6,4,3,1])
print(output)