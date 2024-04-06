def marge(arr, p, q, r):
    """
    Runtime: 340 ms, faster than 43.43% of Python online submissions for Sort an Array.
Memory Usage: 19.1 MB, less than 58.87% of Python online submissions for Sort an Array.
    """
    larray = arr[p:q+1]
    rarray = arr[q+1:r+1]
    i, j = 0, 0
    for k in range(p, r + 1):
        if j < len(rarray) and i < len(larray):
            if larray[i] <= rarray[j]:
                arr[k] = larray[i]
                i += 1
            else:
                arr[k] = rarray[j]
                j += 1
        elif j == len(rarray):
            arr[k] = larray[i]
            i += 1
        elif i == len(larray):
            arr[k] = rarray[j]
            j += 1
def marge_sort(arr, p, r):
    if p < r:
        q = (p + r)//2
        marge_sort(arr, p, q)
        marge_sort(arr, q + 1, r)
        marge(arr, p, q, r)
    return arr
def mergeSort(array):
    return marge_sort(array, 0, len(array)-1)

print(mergeSort([5,4,6,1]))




