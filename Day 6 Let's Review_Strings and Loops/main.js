/**
 * Created by dariusstrasel on 6/7/17.
 */


function processData(input) {
    inputs = input.split(" ");
    inputsList = inputs.slice(1, inputs.length);
    inputsList.forEach(function(element){
        var evenOutput = '';
        var oddOutput = '';
        for (var index = 0; index <= element.length - 1; index++){
            if (index % 2 === 0){
                evenOutput = evenOutput + element[index]
            }
            else {
                oddOutput = oddOutput + element[index]
            }
        }

        var result = evenOutput + " " + oddOutput;
        console.log(result);
    });
}

processData("2 Hacker Rank");