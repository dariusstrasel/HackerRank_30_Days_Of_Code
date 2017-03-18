"""
Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Recursive Method for Calculating Factorial
Task
Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer,  (the argument to pass to factorial).

Constraints

Your submission must contain a recursive function named factorial.
Output Format

Print a single integer denoting .

Sample Input

3
Sample Output

6
Explanation

Consider the following steps:

From steps  and , we can say ; then when we apply the value from  to step , we get . Thus, we print  as our answer."""

def factorial(N):
    result = N
    for num in reversed(range(1, N)):
        result *= num
        print(num, result)
    return result


def recursive_factorial(n, product=False):
    # Base case, input is zero; therefore end of factorial has been reached
    if n == 0 and product is not False:
        print("n == 0 and product is not False")
        return product
    # Secondary case, recursion has started but base case not reached
    if n != 0 and product is False:
        print("n != 0 and product is False")
        product = n * (n - 1)
        return recursive_factorial(n - 2, product)
    # Tertiary case, recursion has occurred at least twice
    if product is not False:
        print("product is not False", product)
        product *= n
        return recursive_factorial(n - 1, product)

print(recursive_factorial(int(input())))
