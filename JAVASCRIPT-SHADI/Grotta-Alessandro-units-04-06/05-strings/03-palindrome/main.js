// Function to reverse a given string
function Reverse(str) {
    let reversed = ""; // Initialize an empty string to store the reversed string
    let length = str.length; // Get the length of the input string
    
    // Loop through the string in reverse order
    while (length > 0) {
        reversed += str.charAt(length - 1); // Append the last character of the string to 'reversed'
        length--; // Decrease the length to move to the previous character
    }
    
    return reversed; // Return the reversed string
}

// Function to check if a string is a palindrome
function isPalindrome(str) {
    // A string is a palindrome if it is equal to its reversed version
    return str === Reverse(str);
}

// Test cases
console.log(isPalindrome("girafarig")); // Output: true (girafarig is a palindrome)
console.log(isPalindrome("giraffa"));   // Output: false (giraffa is not a palindrome)