from collections import Counter

class Solution:
    def isSubset(self, a, b):
        freq = Counter(a)
        for x in b:
            if freq[x] == 0:
                return False
            freq[x] -= 1
        return True
