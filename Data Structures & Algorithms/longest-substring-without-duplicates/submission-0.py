class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        charLastSeen = {} # char -> index last seen

        for i in range(len(s)):
            if (s[i] in charLastSeen) and (charLastSeen[s[i]] >= left):
                left = charLastSeen[s[i]] + 1
            charLastSeen[s[i]] = i
            if (i - left + 1) > best:
                best = i - left + 1
        return best
            


        