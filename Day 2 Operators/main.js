/**
 * Created by dariusstrasel on 3/12/17.
 */
/*
'use strict';

var _input = '';
var _index = 0;
process.stdin.on('data', (data) => { _input += data; });
process.stdin.on('end', () => {
	_input = _input.split(new RegExp('[\n ]+'));
	main(+(_input[0]), +(_input[1]), +(_input[2]));
});
*/

function main(mealCost, tipPercent, taxPercent) {
// My Solution:
    // Write your code here
    var mealCost;
    var tipPercent;
    var taxPercent;

    var tip = mealCost * (tipPercent / 100);
    var tax = mealCost * (taxPercent / 100);

    var totalCost = Number(mealCost + tip + tax).toPrecision(2);
    // Use console.log() to print to stdout
    console.log("The total meal cost is " + totalCost + " dollars.");
}