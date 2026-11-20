class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if (s[start].isalnum() and s[end].isalnum()):
                if (s[start].lower() == s[end].lower()):
                    start = start + 1
                    end = end - 1
                else: 
                    return False
            elif (s[start].isalnum()):
                end = end - 1
            elif (s[end].isalnum()):
                start = start + 1
            else: 
                start = start + 1
                end = end - 1
        return True
        