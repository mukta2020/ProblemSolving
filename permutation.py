def getPermutations(array):
    if len(array) == 1:
        return [array]
    l = []
    for i in range(len(array)):
        el = array[i]
        restarray = array[:i] + array[i+1:]
        subset = getPermutations(restarray)
        for p in subset:
            l.append([el] + p)
    return l

print(getPermutations([1,2,3,4]))

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
print(permutation([1,2,3,4]))

#for p in permutation([1,2,3,4]):
    #print(p)