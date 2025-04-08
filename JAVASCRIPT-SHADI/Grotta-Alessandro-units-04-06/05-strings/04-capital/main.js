// Function to capitalize the first letter of a string
function capital(str) {
    if (!str) return str; // Return the string as is if it's empty or null
    return str.charAt(0).toUpperCase() + str.slice(1); // Capitalize the first letter and append the rest of the string
}

// Example usage:
console.log(capital("pizza salamino")); // Output: "Hello world"