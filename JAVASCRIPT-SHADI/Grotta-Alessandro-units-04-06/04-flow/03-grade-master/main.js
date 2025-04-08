// Declare a variable named numScore without assigning any value
let numScore;

// Define a function named assignGrade that takes one parameter, numScore
function assignGrade(numScore) {
    // Check if numScore is equal to "9"
    if (numScore == "9") {
        // If true, log a message indicating an A grade
        console.log("You get an A, you are great!");
    // Check if numScore is equal to "8"
    } else if (numScore == "8") {
        // If true, log a message indicating a B grade
        console.log("You get a B, congrats!");
    // Check if numScore is equal to "7"
    } else if (numScore == "7") {
        // If true, log a message indicating a C grade
        console.log("You get a C, good job!");
    // Check if numScore is equal to "6"
    } else if (numScore == "6") {
        // If true, log a message indicating a D grade
        console.log("You get a D, you can do better.");
    // Check if numScore is less than or equal to 5
    } else if (numScore <= 5) {
        // If true, log a message indicating an F grade
        console.log("You get an F, you are bad.");
    }
}

// Call the assignGrade function with different scores
assignGrade(7); // Expected output: "You get a C, good job!"
assignGrade(9); // Expected output: "You get an A, you are great!"
assignGrade(4); // Expected output: "You get an F, you are bad."
assignGrade(8); // Expected output: "You get a B, congrats!"