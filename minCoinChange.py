def minNumberOfCoinsForChange(n, denoms):
    nums = [float("inf")] * (n+1)
    nums[0] = 0

    for denom in denoms:
        for i in range(n+1):
            if denom <= i:
                nums[i] = min(nums[i], 1 + nums[i - denom])
    return nums[n] if nums[n] != float("inf") else -1

def numberOfWaysToMakeChange(n, denoms):
    """
    Runtime: 160 ms, faster than 60.17% of Python online submissions for Coin Change 2.
Memory Usage: 13 MB, less than 68.00% of Python online submissions for Coin Change 2.
    :param n:
    :param denoms:
    :return:
    """
    nums = [0] * (n+1)
    nums[0] = 1

    for denom in denoms:
        for i in range(n+1):
            if denom <= i:
                nums[i] += nums[i - denom]
    return nums[n]
print(minNumberOfCoinsForChange(6,[1,5]))
print(numberOfWaysToMakeChange(6, [1, 5]))