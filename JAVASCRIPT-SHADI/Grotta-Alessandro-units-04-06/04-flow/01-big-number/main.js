// Declare two variables, num1 and num2, without assigning any values
let num1;
let num2;

// Define a function named graterNum that takes two parameters, num1 and num2
function graterNum(num1, num2) {
    // Check if num1 is greater than num2
    if (num1 > num2) {
        // If true, log to the console that num1 is greater than num2
        console.log(num1 + " is bigger then " + num2);
    } else {
        // If false, log to the console that num2 is greater than num1
        console.log(num2 + " is bigger then " + num1);
    }
}

// Call the graterNum function with different sets of arguments
graterNum(33, 238451); // Expected output: "238451 is bigger then 33"
graterNum(666, 69);    // Expected output: "666 is bigger then 69"
graterNum(16, 883);    // Expected output: "883 is bigger then 16"