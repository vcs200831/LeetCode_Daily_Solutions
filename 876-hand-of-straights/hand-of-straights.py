from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize
        if len(hand) % groupSize != 0:
            return False

        # Count the frequency of each card
        card_count = Counter(hand)
        
        # Use a min-heap to process cards in order
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first_card = min_heap[0]  # Get the smallest card value
            
            # Try to form a group starting with `first_card`
            for card in range(first_card, first_card + groupSize):
                if card_count[card] == 0:
                    return False
                card_count[card] -= 1
                if card_count[card] == 0:
                    if card != heapq.heappop(min_heap):
                        return False

        return True

# Example usage:
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
sol = Solution()
print(sol.isNStraightHand(hand, groupSize))  # Output: True

hand = [1,2,3,4,5]
groupSize = 4
print(sol.isNStraightHand(hand, groupSize))  # Output: False
