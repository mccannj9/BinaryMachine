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


def general_adder(A, B):
    carry = "0"
    nbits = min(len(A), len(B))
    _sum = ["0"]*(max(len(A), len(B))+1)
    for i in range(nbits):
        a, b = A[-(i+1)], B[-(i+1)]
        ab_sum, carry = full_adder(a, b, carry)
        _sum[-(i+1)] = str(ab_sum)
    _sum[0] = str(carry)
    bin_string = "".join(_sum)
    return bin_string


if __name__ == "__main__":
    import sys
    nums = sys.argv[1:]
    print(len(nums))
    for x in range(0, len(nums), 2):
        A, B = nums[x], nums[x+1]
        _sum = general_adder(A, B)
        print(_sum, convert_bin_to_dec(_sum))

