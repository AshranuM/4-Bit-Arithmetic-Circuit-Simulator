"""
4-bit Full Adder Module
Uses four 1-bit full adders.
"""

def full_adder(a, b, cin):

    # Calculate Sum
    sum_bit = a ^ b ^ cin

    # Calculate Carry
    carry_out = (a & b) | (cin & (a ^ b))

    return sum_bit, carry_out


def four_bit_adder(a, b, cin):

    result = 0
    carry = cin

    # Add four bits one by one
    for i in range(4):

        # Extract individual bits
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1

        # Perform full addition
        sum_bit, carry = full_adder(bit_a, bit_b, carry)

        # Store result bit
        result = result | (sum_bit << i)

    return result, carry