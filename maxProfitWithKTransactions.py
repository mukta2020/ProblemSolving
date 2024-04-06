def maxProfitWithKTransactions(prices, k):
    if len(prices) == 0:
        return 0
    profits = [[0 for d in prices] for t in range(k+1)]
    for t in range(1, k+1):
        maxSoFar = float("-inf")
        for d in range(1, len(prices)):
            maxSoFar = max(maxSoFar, profits[t-1][d-1] -prices[d-1])
            profits[t][d] = max(profits[t][d-1], maxSoFar + prices[d])
    return profits[-1][-1]

def maxProfitWithKTransactions1(prices, k):
    if len(prices) == 0:
        return 0
    evenProfits = [0 for d in prices]
    oddProfits = [0 for d in prices]
    for t in range(1, k+1):
        maxSoFar = float("-inf")
        if t % 2 == 1:
            currentProfits = oddProfits
            previousProfits = evenProfits
        else:
            currentProfits = evenProfits
            previousProfits = oddProfits
        for d in range(1, len(prices)):
            maxSoFar = max(maxSoFar, previousProfits[d-1] -prices[d-1])
            currentProfits[d] = max(currentProfits[d-1], maxSoFar + prices[d])
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        evenProfits = [0 for d in prices]
        oddProfits = [0 for d in prices]
        for t in range(1, k + 1):
            maxSoFar = float("-inf")
            if t % 2 == 1:
                currentProfits = oddProfits
                previousProfits = evenProfits
            else:
                currentProfits = evenProfits
                previousProfits = oddProfits
            for d in range(1, len(prices)):
                maxSoFar = max(maxSoFar, previousProfits[d - 1] - prices[d - 1])
                currentProfits[d] = max(currentProfits[d - 1], maxSoFar + prices[d])
        return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]
print(Solution().maxProfit(2, [3,2,6,5,0,3]))



