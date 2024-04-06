def isValidSubsequence(array, sequence):
   idxa = 0
   idxs = 0
   while idxa < len(array) and idxs < len(sequence):
       if array[idxa] == sequence[idxs]:
           idxs += 1
       idxa += 1
   if idxs == len(sequence):
       return True
   else:
       return False

def isValidSubsequence2(array, sequence):
   idxs = 0
   for a in array:
       if idxs == len(sequence):
           break
       if a == sequence[idxs]:
           idxs += 1
   return idxs == len(sequence)

print(isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))