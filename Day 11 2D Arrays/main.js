/**
 * Created by dariusstrasel on 6/10/17.
 */
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

function getHourglasses(graph){
    var counter = 0
    hourGlasses = []
    graph.forEach(function(rowPosition, rowIndex){
        rowPosition.forEach(function(columnPosition, colIndex, array){
                counter++
                arrayLength = array.length - 2
                console.log(arrayLength, array);
                if (counter === 24 && arrayLength <= 6){
                    console.log("done");
                    console.log(hourGlasses)
                    return hourGlasses;
                }
                else {
                    console.log("else");
                    var hourglass = {
                        topLeft: graph[rowIndex][colIndex],
                        topMid: graph[rowIndex][colIndex + 1],
                        topRight: graph[rowIndex][colIndex + 2],
                        middle: graph[rowIndex + 1][colIndex + 1],
                        botttomLeft: graph[rowIndex + 2][colIndex],
                        bottomMid: graph[rowIndex + 2][colIndex + 1],
                        bottomRight: graph[rowIndex + 2][colIndex + 2]
                    };
                    hourGlasses.push(hourglass);
                    //console.log(counter, hourglass);
                };
            });
        });
};



function main() {
    var arr = [];
    for(arr_i = 0; arr_i < 6; arr_i++){
       arr[arr_i] = readLine().split(' ');
       arr[arr_i] = arr[arr_i].map(Number);
    }
    console.log(getHourglasses(arr));
}


