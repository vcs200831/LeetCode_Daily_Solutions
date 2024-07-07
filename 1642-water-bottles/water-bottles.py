class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = numBottles
        emptyBottles = numBottles
    
        while emptyBottles >= numExchange:
            newFullBottles = emptyBottles // numExchange
            totalDrank += newFullBottles
            emptyBottles = emptyBottles % numExchange + newFullBottles
    
        return totalDrank
        