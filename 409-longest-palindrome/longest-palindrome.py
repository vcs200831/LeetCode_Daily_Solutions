class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        return sum(v // 2 * 2 for v in Counter(s).values()) + (any(v % 2 for v in Counter(s).values()))
        