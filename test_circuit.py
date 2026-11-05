"""
Testing all four operations of the 4-bit Arithmetic Circuit.
"""

from arithmetic_circuit import perform_operation


def test_circuit():

    print("=" * 55)
    print("       4-BIT ARITHMETIC CIRCUIT TESTING")
    print("=" * 55)

    operations = [
        (0, 0, "Addition"),
        (0, 1, "Subtraction"),
        (1, 0, "Increment"),
        (1, 1, "Decrement")
    ]

    for s1, s0, name in operations:

        print("\nTesting:", name)

        passed = 0
        total_tests = 0

        # Test all possible A and B values
        for a in range(16):
            for b in range(16):

                operation, y, cin, result, carry = perform_operation(
                    a, b, s1, s0
                )

                # Calculate expected result
                if s1 == 0 and s0 == 0:
                    expected = a + b

                elif s1 == 0 and s0 == 1:
                    expected = a - b

                elif s1 == 1 and s0 == 0:
                    expected = a + 1

                else:
                    expected = a - 1

                # Compare 4-bit result
                expected_result = expected & 15

                # Check carry according to adder output
                expected_carry = (a + y + cin) >> 4

                total_tests += 1

                if (result == expected_result and
                        carry == expected_carry):
                    passed += 1

        print("Tests Passed :", passed)
        print("Total Tests  :", total_tests)

        if passed == total_tests:
            print("Status       : PASSED")
        else:
            print("Status       : FAILED")

    print("\n" + "=" * 55)
    print("             TESTING COMPLETED")
    print("=" * 55)


if __name__ == "__main__":
    test_circuit()