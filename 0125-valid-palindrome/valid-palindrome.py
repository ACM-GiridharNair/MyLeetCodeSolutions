class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                t += c
        return ''.join(reversed(t.lower())) == t.lower()
        