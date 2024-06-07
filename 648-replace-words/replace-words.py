from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Convert list of roots to a set for efficient lookups
        root_set = set(dictionary)
        
        # Helper function to replace a word with its shortest root prefix
        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]  # Return the shortest matching root
            return word  # Return the word itself if no root prefix is found
        
        # Split the sentence into words, replace each word, and join them back into a sentence
        return ' '.join(map(replace, sentence.split()))

# Example usage:
solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(solution.replaceWords(dictionary, sentence))
# Output: "the cat was rat by the bat"
