"""
Multiplexer Module
Selects Y and Cin using control lines S1 and S0.
"""

def select_inputs(a, b, s1, s0):

    # Addition: S1S0 = 00
    if s1 == 0 and s0 == 0:
        y = b
        cin = 0
        operation = "Addition"

    # Subtraction: S1S0 = 01
    elif s1 == 0 and s0 == 1:
        y = b ^ 15
        cin = 1
        operation = "Subtraction"

    # Increment: S1S0 = 10
    elif s1 == 1 and s0 == 0:
        y = 0
        cin = 1
        operation = "Increment"

    # Decrement: S1S0 = 11
    else:
        y = 15
        cin = 0
        operation = "Decrement"

    return y, cin, operation