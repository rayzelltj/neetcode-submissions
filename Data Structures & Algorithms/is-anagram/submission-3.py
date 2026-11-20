class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            return sorted(s) == sorted(t)

            # conceptually the same as below, python is simpler:
            # sortedS = sorted(s) 
            # sortedT = sorted(t)
            # for i in range(len(s)):
            #     if (sortedS[i] != sortedT[i]):
            #         return False
            # return True
        