class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # (window size) − (count of its most common letter) ≤ k
        count = {} # char -> occurences
        res = 0 
        maxf = 0
        left = 0

        for right, char in enumerate(s):
            if char in count: 
                count[char] = count[char] + 1
            else:
                count[char] = 1
            # count[char] = 1 + count.get(char, 0)
            
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] = count[s[left]] - 1
                left = left + 1

            res = max(res, right - left + 1)
        return res