/*
    This function takes a number as input and returns a string representing the amount in dollars.
    If the input is 1 million, it appends a smiley face to the result.
    Invalid inputs (non-numbers or negative values) return an error message.
*/

function money(amount) {
    // Validate the input: it must be a non-negative number
    if (typeof amount !== "number" || amount < 0) return "Invalid amount!";
    
    // Decide whether to use "euro" (singular) or "euros" (plural) based on the amount
    let dollarText = amount === 1 ? "euro" : "euros";
    
    // Include a smiley face if the amount is exactly 1 million
    let smiley = amount === 1000000 ? " :D" : "";
    
    // Return the formatted string with the amount, dollar text, and optional smiley
    return `${amount} ${dollarText}${smiley}`;
}
// Example usage:
console.log(money(1));        // Output: "1 euro"
console.log(money(10));       // Output: "10 euros"
console.log(money(1000000));  // Output: "1000000 euros ;)"
console.log(money(-5));       // Output: "Invalid amount!"
console.log(money("wassup"));  // Output: "Invalid amount!"