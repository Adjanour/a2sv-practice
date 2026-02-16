class Solution:
    def checkEqual(self, a, b) -> bool:
        
        if len(a) != len(b):
            return False

        freq = {}

        # Count elements in a
        for x in a:
            freq[x] = freq.get(x, 0) + 1
                
        
        # check if elements exist
        for x in b:
            if x not in b:
                return False
                
            freq[x] -= 1
            
            if freq[x] < 0:
                return False
                
        
        return True
            