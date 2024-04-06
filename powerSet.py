def powerset(array):
    if len(array) == 0:
        return [[]]
    l = [[]]
    for i in range(len(array)):
        m = array[i]
        l.append([m])
        if len(array[i+1:]) > 0:
            for p in powerset(array[i+1:]):
                if p:
                    l.append([m] + p)
    return l
#print(powerset([1, 2, 3]))

def powersetCorrect(array):
    if len(array) == 0:
        return [[]]
    l = [[]]
    for i in range(len(array)):
        m = array[i]
        l.append([m])
        for p in powersetCorrect(array[i+1:]):
            if p: l.append([m] + p)
    return sorted(l, key=len)
#print(powersetCorrect([1,2,3]))
def power(array):
    if len(array) == 0:
        return [[]]
    fst = array[0]
    remaining = array[1:]
    allSet = []
    pset = power(remaining)
    for subSet in pset:
        allSet.append(subSet)
        allSet.append([fst] + subSet)
    #return sorted(allSet, key=len)
    return  allSet
print(power([1,2,3]))
def powerset_Algo2(array):
    s = [[]]
    for ele in array:
        for i in range(len(s)):
            current = s[i]
            s.append(current + [ele])
    #return sorted(s, key=len)
    return s
print(powerset_Algo2([1,2,3]))

def get_power_set(array):
    s = [[]]
    for elem in array:
        for sub_set in s:
            s = s + [list(sub_set) + [elem]]
    return sorted(s, key=len)

#print(get_power_set([1,2,3]))



def powersetStack(s):
    x = len(s)
    for i in range(1 << x):
        print([s[j] for j in range(x) if (i & (1 << j))])
#powersetStack([1,2,3])