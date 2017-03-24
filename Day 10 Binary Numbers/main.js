/**
 * Created by dariusstrasel on 3/19/17.
 */

function convertToBinary(inputNumber) {
    var quotient = inputNumber;
    var result = [];
    var result_reversed = [];
    while (quotient != 0) {
        var remainder = quotient % 2;
        result.push(remainder);
        quotient = Math.floor(quotient / 2);
    }

    for (var index = result.length; index < -1; index--){
        result_reversed.push(result[index]);
    }
    var binary = result_reversed.join("");
    return binary;


    /*
    result = []
    product = number
    while product is not 0:
        # print("Loop: ", product)
        remainder = (product % 2)
        result.append(str(remainder))
        product = (product // 2)
    binary = "".join(reversed(result))
    return binary
    */
}

console.log(convertToBinary(5));