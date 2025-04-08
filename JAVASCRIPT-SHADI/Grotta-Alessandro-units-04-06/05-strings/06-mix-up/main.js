function mixUp(str1, str2) {
    // Check if both strings are at least 2 characters long
    if (str1.length < 2 || str2.length < 2) return "Strings must be at least 2 characters long";

    // Swap the first 2 characters of the strings
    let swapped1 = str2.slice(0, 2) + str1.slice(2); // Take the first 2 letters of str2 and combine with the rest of str1
    let swapped2 = str1.slice(0, 2) + str2.slice(2); // Take the first 2 letters of str1 and combine with the rest of str2

    // Return the swapped strings as a single string
    return `${swapped1} ${swapped2}`;
}

// Example usage:
console.log(mixUp('gold', 'digger'));      // Swap first 2 letters: "pox mid"
console.log(mixUp('pokemon', 'smerald'));   // Swap first 2 letters: "dig donner"
console.log(mixUp('batman', 'catwoman'));  // Swap first 2 letters: "wollo herld"
