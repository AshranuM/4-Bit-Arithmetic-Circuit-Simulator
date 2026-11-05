"""
Main Arithmetic Circuit
Connects Multiplexer and 4-bit Full Adder.
"""

from multiplexer import select_inputs
from full_adder import four_bit_adder


def perform_operation(a, b, s1, s0):

    # Restrict inputs to 4 bits
    a = a & 15
    b = b & 15

    # Select Y and Cin using multiplexer
    y, cin, operation = select_inputs(a, b, s1, s0)

    # Perform addition using 4-bit full adder
    result, carry_out = four_bit_adder(a, y, cin)

    # Return all important values
    return operation, y, cin, result, carry_out