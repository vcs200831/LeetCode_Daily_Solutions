class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits in the binary representation of num
        num_bits = num.bit_length()
        
        # Create a bitmask with all bits set to 1, which is the same length as num
        bitmask = (1 << num_bits) - 1
        
        # XOR num with the bitmask to flip all the bits
        return num ^ bitmask
