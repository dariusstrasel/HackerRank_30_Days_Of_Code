#!/bin/python3

"""Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is ."""


import sys
import re
import math

n = int(input().strip())


def convert_to_binary(number):
    result = []
    product = number
    while product is not 0:
        # print("Loop: ", product)
        remainder = (product % 2)
        result.append(str(remainder))
        product = (product // 2)
    binary = "".join(reversed(result))
    return binary


def consecutive_ones(number):
    consecutive_pattern = "1{1,}"
    number = str(number)
    pattern_result = re.findall(consecutive_pattern, number)
    if pattern_result:
        largest_consecutive_one_size = max([len(item) for item in pattern_result])
        return largest_consecutive_one_size
    else:
        return 1


def main(input_number):
    input_as_binary = convert_to_binary(input_number)
    consecutive_ones_of_input = consecutive_ones(input_as_binary)
    return consecutive_ones_of_input


print(main(n))