def longestPeak(array):
    f, b = 1, 0
    longestPeakLength = 0
    peak = False
    for i in range(1, len(array) - 1):
        if not peak:  # strictly increasing counting
            if array[i-1] < array[i]:
                f += 1
            else:
                f = 1

        if array[i-1] < array[i] > array[i + 1]:
            if peak:
                longestPeakLength = max(longestPeakLength, f + b)
                f = b + 1  # peak in between another peak
                b = 0
            peak = True

        elif peak:  # strictly decresing counting
            if array[i - 1] > array[i]:
               b += 1
            else:
                longestPeakLength = max(longestPeakLength, f + b)
                f = 1
                b = 0
                peak = False

    if peak and array[-1] < array[-2]:
        b = b + 1
    if peak:
        return max(longestPeakLength, f + b)
    else:
        return longestPeakLength


print(longestPeak([1,3,2]))

#[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
#[1,2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2,3, 4, 5, 0, -1, -1]
