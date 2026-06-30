class SumIntegersSolution:
    def get_sum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        
        # Mask inputs to 32 bits unsigned
        a = a & 0xffffffff
        b = b & 0xffffffff

        for i in range(32):
            first_bit = self._get_bit(a, i)
            second_bit = self._get_bit(b, i)

            sum_bit = first_bit ^ second_bit ^ carry
            result = self._update_bit(result, i, sum_bit)
            
            if (first_bit == 1 and second_bit == 1) or                (first_bit == 1 and carry == 1) or                (carry == 1 and second_bit == 1):
                carry = 1
            else:
                carry = 0

        # Convert back to signed 32-bit
        if result >= 0x80000000:
            return result - 0x100000000
        return result

    def _get_bit(self, number: int, i: int) -> int:
        return (number >> i) & 1

    def _update_bit(self, number: int, i: int, bit: int) -> int:
        clear_mask = (~(1 << i)) & 0xffffffff
        return (number & clear_mask) | (bit << i)
