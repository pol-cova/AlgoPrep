class ReverseIntSolution:
    def reverse_bits(self, n: int) -> int:
        # Work with 32-bit unsigned during processing
        n = n & 0xffffffff
        for i in range(16):
            first_bit = self._get_bit(n, i)
            second_bit = self._get_bit(n, 31 - i)
            
            n = self._update_bit(n, i, second_bit)
            n = self._update_bit(n, 31 - i, first_bit)
            
        # Convert back to signed 32-bit integer
        if n >= 0x80000000:
            return n - 0x100000000
        return n

    def _get_bit(self, n: int, i: int) -> int:
        return (n >> i) & 1

    def _update_bit(self, n: int, i: int, bit: int) -> int:
        clear_bit_mask = (~(1 << i)) & 0xffffffff
        return (n & clear_bit_mask) | (bit << i)
