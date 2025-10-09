class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit=0
        buy=prices[0]
        for sell in prices[1:]:
            if sell > buy :
                profit = max(profit,sell - buy)
            else :
                buy = sell
                
        return profit
            
s= Solution()
print(s.maxProfit([7,1,5,3,6,4]))