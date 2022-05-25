class Solution:

    def expandFromMiddle(self, s:str, left : int, right : int):
        if s == None or left > right:
            # No palindrome in substring to return
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ''

        # boundaries
        start = 0
        end = 0

        for i in range(len(s) - 1):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - ((length - 1) // 2)
                end = i + (length // 2)


        return s[start : end + 1]

sl = Solution()
print(sl.longestPalindrome("babad"))
print(sl.longestPalindrome("ccc"))
# Ex. 1
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Ex. 2
# Input: s = "cbbd"
# Output: "bb"