// Declare a variable with global scope
let globalResult;

// Function to add two numbers and store the result in a global variable
function addNumbers2(num3, num4) {
    // Calculate the sum and store it in the global variable
    globalResult = num3 + num4;
    // Log the global result to the console
    console.log("The global result is: " + globalResult);
}

// Call the function with arguments 5 and 9
addNumbers2(5, 9);

// Function to add two numbers and store the result in a local variable
function addNumbers(num1, num2) {
    // Declare a variable with local scope to hold the result
    let localResult = num1 + num2;
    // Log the local result to the console
    console.log("The local result is: " + localResult);
}

// Call the function with arguments 2 and 6
addNumbers(2, 6);