class NumberConversionSolution:
    def number_of_bits_to_flip_to_convert(self, a: int, b: int) -> int:
        a = a & 0xffffffff
        b = b & 0xffffffff
        number_of_bits_to_flip = 0
        while a != 0 or b != 0:
            bit_from_a = a & 1
            bit_from_b = b & 1
            if bit_from_a != bit_from_b:
                number_of_bits_to_flip += 1
            a >>= 1
            b >>= 1
        return number_of_bits_to_flip
