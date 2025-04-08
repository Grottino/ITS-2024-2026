// Function to replace all occurrences of the first character in a string (except the first one) with '*'
function fixStart(str) {
    if (str.length < 1) return str; // If the string is empty, return it as is

    let firstChar = str.charAt(0); // Get the first character of the string
    let result = firstChar; // Start the result with the first character

    // Loop through the rest of the string
    for (let i = 1; i < str.length; i++) {
        // If the current character matches the first character, replace it with '*'
        // Otherwise, keep the character as is
        result += (str.charAt(i) === firstChar) ? '*' : str.charAt(i);
    }
    
    return result; // Return the modified string
}

// Example usage:
console.log(fixStart('peperoni'));  // Output: "pe*eroni" (all 'p's after the first are replaced with '*')
console.log(fixStart('character'));  // Output: "chara*ter" (all 'c's after the first are replaced with '*')
console.log(fixStart('sunshine'));   // Output: "sun*hine" (all 's's after the first are replaced with '*')
console.log(fixStart('villain'));  // Output: "vil*ain" (all 'l's after the first are replaced with '*')