/**
 * Created by dariusstrasel on 3/12/17.
 */
/*
* Objective
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
Explanation

Sample Case 0:
 is odd and odd numbers are weird, so we print Weird.

Sample Case 1:
 and  is even, so it isn't weird. Thus, we print Not Weird.
* */

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var N = parseInt(readLine());
    if (N != undefined || N != "") {
        var answer = ""
        if (N % 2 != 0) {
            answer = "Weird"
            }
        else if (N > 20 || N >= 2 && N <= 5){
            answer = "Not Weird"
            }
        else {
            answer = "Weird"
            }
        console.log(answer)
    }
}