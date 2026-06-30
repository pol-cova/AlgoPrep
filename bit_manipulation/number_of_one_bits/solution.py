class NumberOfOneBitsSolution:
    def number_of_one_bits(self, n: int) -> int:

        n = n & 0xffffffff
        bit_count = 0
        while n != 0:
            bit_count += (n & 1)
            n >>= 1
        return bit_count
