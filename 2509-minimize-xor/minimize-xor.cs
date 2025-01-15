using System;

class Solution {
    public int MinimizeXor(int num1, int num2) {
        int targetBits = CountSetBits(num2); // Step 1
        int x = 0;
        
        // Set bits in `x` based on `num1` to minimize XOR
        for (int i = 31; i >= 0 && targetBits > 0; i--) {
            if ((num1 & (1 << i)) != 0) { // Check if the bit is set in num1
                x |= (1 << i); // Set the same bit in x
                targetBits--;   // Reduce target bits
            }
        }
        
        // If more bits are needed, set the smallest unset bits in `x`
        for (int i = 0; i <= 31 && targetBits > 0; i++) {
            if ((x & (1 << i)) == 0) { // Check if the bit is not set in x
                x |= (1 << i); // Set the bit in x
                targetBits--;  // Reduce target bits
            }
        }
        
        return x;
    }

    private int CountSetBits(int n) {
        int count = 0;
        while (n > 0) {
            count += (n & 1); // Add 1 if the least significant bit is set
            n >>= 1;          // Right shift to process the next bit
        }
        return count;
    }
}
