//Setting variables
let decimalInput = document.getElementById("dec-inp"); //Creating of variables
let binaryOutput = document.getElementById("bin-out");

function DecimalToBinary(decimalNumber) { //Creating of function and defining of an input
  if (isNaN(decimalNumber)) {
    return "Please enter a valid number.";
  }

  if (decimalNumber < 0) {
    return "Negative numbers cannot be converted to the binary system.";
  }

  if (decimalNumber === 0) {
    return "0";
  }

  var binary = "";
  while (decimalNumber > 0) {
    var remainder = decimalNumber % 2;
    binary = remainder + binary;
    decimalNumber = Math.floor(decimalNumber / 2);
  }

  return binary;
  
}
//Insert the output of DecimalToBinary function into the binary ouput field
decimalInput.addEventListener("input", () => {
    binaryOutput.value = DecimalToBinary(decimalInput.value)
  });