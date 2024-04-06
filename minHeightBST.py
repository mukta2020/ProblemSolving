def minHeightBst(array):
    return minHeightHelper(array, None, 0, len(array) - 1)

def minHeightHelper(array, bst, low, high):
    if high < low:
        return
    mid = (low + high)//2
    if bst is None:
        bst = BST(array[mid])
    else:
        bst.insert(array[mid])
    minHeightHelper(array, bst, low, mid - 1)
    minHeightHelper(array, bst, mid + 1, high)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])
