
def to_binary(n):
    return format(n & 0xFF, '08b')


def signed_arithmetic(a, b):
    # Subtract b from a using 8-bit 2's complement
    binary_a = to_binary(a)
    binary_b = to_binary(b)
    negative_b = to_binary(-b)

    # Perform 8-bit binary addition
    unsigned_result = (a & 0xFF) + ((-b) & 0xFF)
    result = unsigned_result & 0xFF

    # Convert the 8-bit result back to signed decimal
    if result >= 128:
        decimal_result = result - 256
    else:
        decimal_result = result

    # Overflow occurs if the mathematical result is out of range
    actual_result = a - b
    overflow = actual_result < -128 or actual_result > 127

    print("Operand A:", binary_a, "(", a, ")")
    print("Operand B:", binary_b, "(", b, ")")
    print("2's complement of B:", negative_b)
    print("Binary addition:",
          binary_a, "+", negative_b)
    print("Final result:", format(result, '08b'))
    print("Decimal result:", decimal_result)
    print("Overflow:", "Yes" if overflow else "No")
    print("-" * 35)


print("a) 45 - (+19)")
signed_arithmetic(45, 19)

print("b) (-35) - (-12)")
signed_arithmetic(-35, -12)
