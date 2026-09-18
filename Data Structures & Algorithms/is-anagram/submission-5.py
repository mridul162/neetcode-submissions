class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash={}    

        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        for i in t:
            if i in hash:
                hash[i] -= 1
            else:
                return False

        return all(value == 0 for value in hash.values())
        