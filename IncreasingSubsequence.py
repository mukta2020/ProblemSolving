def maxSumIncreasingSubsequence1(array):
    sums = [array[0]]
    sequence = [None]
    maxsum = array[0]
    idx = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] > array[j]:
                temp = array[i] + sums[j]
                if j == 0:
                    sums.append(temp)
                    sequence.append(j)
                if array[i] > temp:
                    sums[i] = array[i]
                    sequence[i] = None
                elif temp > sums[i]:
                    sums[i] = temp
                    sequence[i] = j
            elif j == 0:
                sums.append(array[i])
                sequence.append(None)
        if sums[i] > maxsum:
            maxsum, idx = sums[i], i

    seq = [array[idx]]
    while idx is not None:
        idx = sequence[idx]
        if idx is not None:
            seq.append(array[idx])
    return [maxsum, seq[::-1]]

def maxSumIncreasingSubsequence(array):
    sums = array[:]
    sequence = [None for x in array]
    maxsum = array[0]
    idx = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] > array[j]:
                temp = array[i] + sums[j]
                if temp > sums[i]:
                    sums[i] = temp
                    sequence[i] = j
        if sums[i] > maxsum:
            maxsum, idx = sums[i], i

    seq = [array[idx]]
    while idx is not None:
        idx = sequence[idx]
        if idx is not None:
            seq.append(array[idx])
    return [maxsum, seq[::-1]]


print(maxSumIncreasingSubsequence([8,12,2,3,15,5,7]))
#[10, 70, 20, 30, 50, 11, 30]
# [8,12,2,3,15,5,7]
#[-1,1]

