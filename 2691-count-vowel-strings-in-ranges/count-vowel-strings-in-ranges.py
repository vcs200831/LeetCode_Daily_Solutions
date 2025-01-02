class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Helper function to check if a character is a vowel
        def is_vowel(ch):
            return ch in {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize prefix sum array
        n = len(words)
        prefix = [0] * n
        
        # Fill prefix array
        for i, word in enumerate(words):
            if is_vowel(word[0]) and is_vowel(word[-1]):  # Check if word starts and ends with a vowel
                prefix[i] = 1
            if i > 0:
                prefix[i] += prefix[i-1]  # Add to prefix sum
        
        # Answer queries
        result = []
        for li, ri in queries:
            if li == 0:
                result.append(prefix[ri])  # Use the prefix sum directly
            else:
                result.append(prefix[ri] - prefix[li-1])  # Subtract to get count in range
        
        return result
