// Function to reverse a given string and return it
function Reverse(str) {
    let reversed = ""; // Initialize an empty string to store the reversed result
    let length = str.length; // Get the length of the input string
    
    // Loop through the string in reverse order
    while (length > 0) {
        reversed += str.charAt(length - 1); // Append the last character of the string to 'reversed'
        length--; // Decrease the length to move to the previous character
    }
    return reversed; // Return the reversed string
}

// Test the function with sample strings and print the results
console.log(Reverse("Guantanamera")); // Expected output: "aremanatnauG"
console.log(Reverse("Batman"));       // Expected output: "namtaB"