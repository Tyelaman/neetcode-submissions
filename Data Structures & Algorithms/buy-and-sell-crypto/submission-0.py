class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0

        for price in prices:
            while stack and price < stack[-1]:
                stack.pop()

            stack.append(price)
            current_profit = price - stack[0]
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit