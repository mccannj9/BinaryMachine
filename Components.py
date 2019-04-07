#! /usr/bin/env python3


def and_gate(A, B):
    return str(int(A) and int(B))


def xor_gate(A, B):
    return str(int(A) ^ int(B))


def or_gate(A, B):
    return str(int(A) or int(B))


def half_adder(A, B):
    return xor_gate(A, B), and_gate(A, B)


def full_adder(A, B, carry_in):
    ha1 = half_adder(A, B)
    ha2 = half_adder(carry_in, ha1[0])
    sum_out = ha2[0]
    carry_out = or_gate(ha1[1], ha2[1])

    return sum_out, carry_out


def convert_bin_to_dec(bin_string):
    output = 0
    for exp, num in enumerate(bin_string[::-1]):
        output += (2**exp)*int(num)
    return output


if __name__ == "__main__":
    # add two one-bit numbers
    print("Adding 1 + 1")
    A = '1'
    B = '1'
    C = '0'
    sum_out, carry_out = full_adder(A, B, C)
    bin_string = f"{carry_out}{sum_out}"
    print(bin_string, convert_bin_to_dec(bin_string))

    print("Adding 1 + 0")
    A = '1'
    B = '0'
    C = '0'
    sum_out, carry_out = full_adder(A, B, C)
    bin_string = f"{carry_out}{sum_out}"
    print(bin_string, convert_bin_to_dec(bin_string))

    print("Adding 0 + 1")
    A = '0'
    B = '1'
    C = '0'
    sum_out, carry_out = full_adder(A, B, C)
    bin_string = f"{carry_out}{sum_out}"
    print(bin_string, convert_bin_to_dec(bin_string))

    print("Adding 0 + 0")
    A = '0'
    B = '0'
    C = '0'
    sum_out, carry_out = full_adder(A, B, C)
    bin_string = f"{carry_out}{sum_out}"
    print(bin_string, convert_bin_to_dec(bin_string))

    # add two two bit numbers
    A = "10"
    B = "11"
    carry_in_1 = '0'
    expect = "101"
    sum_out_1, carry_in_2 = full_adder(A[1], B[1], carry_in_1)
    sum_out_2, carry_out = full_adder(A[0], B[0], carry_in_2)
    bin_string = f"{carry_out}{sum_out_2 + sum_out_1}"
    print(
        bin_string, convert_bin_to_dec(bin_string),
        convert_bin_to_dec(expect)
    )

    eight_bit_A = "10001001"
    eight_bit_B = "00110101"
    nine_bit_sum = list("000000000")
    carry = "0"
    nbits = 8
    for i in range(nbits):
        a, b = eight_bit_A[-(i+1)], eight_bit_B[-(i+1)]
        ab_sum, carry = full_adder(a, b, carry)
        nine_bit_sum[-(i+1)] = str(ab_sum)
    nine_bit_sum[0] = str(carry)
    bin_string = "".join(nine_bit_sum)
    print(bin_string, convert_bin_to_dec(bin_string))

    A = bin(255)[2:]
    B = bin(213)[2:]
    carry = "0"
    nbits = min(len(A), len(B))
    _sum = ["0"]*(max(len(A), len(B))+1)
    for i in range(nbits):
        a, b = A[-(i+1)], B[-(i+1)]
        ab_sum, carry = full_adder(a, b, carry)
        _sum[-(i+1)] = str(ab_sum)
    _sum[0] = str(carry)
    bin_string = "".join(_sum)
    print(bin_string, convert_bin_to_dec(bin_string))

