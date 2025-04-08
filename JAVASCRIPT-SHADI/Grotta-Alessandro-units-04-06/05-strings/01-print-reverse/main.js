// Function to reverse a given string and print it
function printReverse(str) {
    let reversed = ""; // Initialize an empty string to store the reversed result
    let length = str.length; // Get the length of the input string
    
    // Loop through the string in reverse order
    while (length > 0) {
        reversed += str.charAt(length - 1); // Append the last character of the string to 'reversed'
        length--; // Decrease the length to move to the previous character
    }
    
    console.log(reversed); // Print the reversed string
}

// Test the function with sample strings
printReverse("Guantanamera"); // Expected output: "aremanatnauG"
printReverse("Batman");       // Expected output: "namtaB"