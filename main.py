"""
Main Controller for 4-bit Arithmetic Circuit Simulator.
"""

from arithmetic_circuit import perform_operation


# Function to accept valid 4-bit input
def get_input(message):

    while True:

        try:
            number = int(input(message))

            if 0 <= number <= 15:
                return number

            print("Enter a number between 0 and 15.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Main program
def main():

    print("=" * 50)
    print("       4-BIT ARITHMETIC CIRCUIT SIMULATOR")
    print("=" * 50)

    while True:

        print("\nSelect an Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Increment")
        print("4. Decrement")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        # Exit
        if choice == "5":
            print("Exiting Simulator.")
            break

        # Check valid choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        # Take inputs
        a = get_input("Enter value of A (0-15): ")

        if choice == "1" or choice == "2":
            b = get_input("Enter value of B (0-15): ")
        else:
            b = 0

        # Select control lines
        if choice == "1":
            s1, s0 = 0, 0

        elif choice == "2":
            s1, s0 = 0, 1

        elif choice == "3":
            s1, s0 = 1, 0

        else:
            s1, s0 = 1, 1

        # Perform arithmetic operation
        operation, y, cin, result, carry = perform_operation(
            a, b, s1, s0
        )

        # Display results
        print("\n" + "-" * 50)
        print("          CALCULATION RESULT")
        print("-" * 50)

        print("Operation :", operation)
        print("Control S1 :", s1)
        print("Control S0 :", s0)

        print("Operand A  :", format(a, "04b"))

        if choice == "1" or choice == "2":
            print("Operand B  :", format(b, "04b"))

        print("Selected Y :", format(y, "04b"))
        print("Carry In   :", cin)

        print("-" * 50)

        print("Binary Result  :", format(result, "04b"))
        print("Decimal Result :", result)
        print("Carry Out      :", carry)

        # Signed interpretation for subtraction
        if choice == "2" and result >= 8:
            print("Signed Result :", result - 16)
        elif choice == "2":
            print("Signed Result :", result)

        print("-" * 50)


if __name__ == "__main__":
    main()