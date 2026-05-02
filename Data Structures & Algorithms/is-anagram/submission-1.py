class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i in letters.keys():
                letters[i] += 1
            else:
                letters[i] = 1
        
        for i in t:
            if i in letters.keys():
                letters[i] -= 1
            else:
                return False
        
        for i in letters.values():
            if i != 0:
                return False
        return True
                
    # Time = O(n)
    # Space = O(n)
        