class Solution:
    def maxProfit(self, prices: list()) -> int:
        left, right = 0, 1
        maximumProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left]
                maximumProfit = max (maximumProfit, currentProfit)
            else:
                left = right
            right += 1

        return maximumProfit

if __name__ == '__main__':
    sol = Solution ()
    prices = [7, 1, 5, 3, 4, 6]
    maxProf = sol.maxProfit (prices)
    print (maxProf) 