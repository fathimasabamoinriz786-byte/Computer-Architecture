
def rol(binary, positions):
    print("\nROL - Rotate Left Without Carry")
    print("Original number:", binary)

    for i in range(positions):
        leftmost = binary[0]
        binary = binary[1:] + leftmost
        print("After rotation", i + 1, ":", binary)

    print("Final result:", binary)


def rcl(binary, carry, positions):
    print("\nRCL - Rotate Left Through Carry")
    print("Original number:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        leftmost = binary[0]
        binary = binary[1:] + carry
        carry = leftmost

        print("After rotation", i + 1, ":", binary)
        print("Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)


number = "10110110"

rol(number, 2)

# Assume the initial carry flag is 0
rcl(number, "0", 2)
