

def to_binary(n):
    return format(n & 0xFF, '08b')


def signed_arithmetic(a, b, operation):
    if operation == '+':
        result_full = (a & 0xFF) + (b & 0xFF)
        actual_result = a + b
    else:
        result_full = (a & 0xFF) + ((-b) & 0xFF)
        actual_result = a - b

    result = result_full & 0xFF

    if result >= 128:
        decimal_result = result - 256
    else:
        decimal_result = result

    overflow = actual_result < -128 or actual_result > 127

    print("Operand A:", to_binary(a), "(", a, ")")
    print("Operand B:", to_binary(b), "(", b, ")")

    if operation == '+':
        print("Operation: Addition")
        print("Binary calculation:",
              to_binary(a), "+", to_binary(b))
    else:
        print("Operation: Subtraction")
        print("2's complement of B:", to_binary(-b))
        print("Binary calculation:",
              to_binary(a), "+", to_binary(-b))

    print("Final binary result:", to_binary(decimal_result))
    print("Final decimal result:", decimal_result)
    print("Overflow:", "Yes" if overflow else "No")
    print("-" * 40)


print("a) +46 + (+29)")
signed_arithmetic(46, 29, '+')

print("b) (-48) - (-23)")
signed_arithmetic(-48, -23, '-')
