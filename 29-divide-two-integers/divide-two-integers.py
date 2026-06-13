class Solution(object):
    def divide(self, dividend, divisor):
        
        # Overflow case
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        # Sign determine karo
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Positive numbers me convert karo
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Divisor ko powers of 2 se double karo
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        return sign * result