
def groupAnagrams(words):
    from collections import defaultdict
    ans = defaultdict(list)
    for s in words:
        count = [0] * 26
        for c in s:
            u1 = ord(c)
            u2 = ord('a')
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    retVal = []
    for v in ans.values():
        retVal.append(v)
    return retVal
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))