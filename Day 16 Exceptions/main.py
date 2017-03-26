#!/bin/python3

import sys

def main(input):
    try:
        int(input)
        print(input)
    except ValueError:
        print("Bad String")

S = input().strip()

main(S)