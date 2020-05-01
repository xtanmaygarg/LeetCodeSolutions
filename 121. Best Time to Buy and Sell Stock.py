class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        Profit = 0
        Curr_Min = prices[0]
        
        for value in prices:
            Curr_Min = min(value, Curr_Min)
            Profit = max(Profit, value - Curr_Min)
        
        return Profit
