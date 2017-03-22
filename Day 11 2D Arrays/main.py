"""
Objective
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""

#!/bin/python3

import sys


def collect_arguments():
    inputs_as_list = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        inputs_as_list.append(arr_t)
    return inputs_as_list


def return_largest_hourglass_sum():
    graph = collect_arguments()
    col_length = len(graph[0])
    row_length = len(graph)

    hourglass_sums = [[graph[row_position][col_position] + graph[row_position][col_position + 1] + graph[row_position][
        col_position + 2] + graph[row_position + 1][col_position + 1] + graph[row_position + 2][col_position] +
                       graph[row_position + 2][col_position + 1] + graph[row_position + 2][col_position + 2]] for
                      col_position in range(col_length - 2) for row_position in range(row_length - 2)]

    max_hourglass_sum = max(hourglass_sums)[0]

    print(max_hourglass_sum)


return_largest_hourglass_sum()
