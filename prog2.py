

def ror(binary, positions):
    print("\nROR - Rotate Right Without Carry")
    print("Original number:", binary)

    for i in range(positions):
        rightmost = binary[-1]
        binary = rightmost + binary[:-1]
        print("After rotation", i + 1, ":", binary)

    print("Final result:", binary)


def rcr(binary, carry, positions):
    print("\nRCR - Rotate Right Through Carry")
    print("Original number:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        rightmost = binary[-1]
        binary = carry + binary[:-1]
        carry = rightmost

        print("After rotation", i + 1, ":", binary)
        print("Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)


number = "11010101"

ror(number, 3)

# Assume the initial carry flag is 0
rcr(number, "0", 3)
