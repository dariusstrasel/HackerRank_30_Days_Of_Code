/**
 * Created by dariusstrasel on 6/7/17.
 */


function processData(input) {
    var evenOutput = ''
    var oddOutput = ''
    for (var index = 1; index <= input.length - 1; index++){
        if (index % 2 === 0){
            evenOutput = evenOutput + input[index]
        }
        else {
            oddOutput = oddOutput + input[index]
        }
    }
    result = evenOutput + " " + oddOutput
    console.log(result);
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});