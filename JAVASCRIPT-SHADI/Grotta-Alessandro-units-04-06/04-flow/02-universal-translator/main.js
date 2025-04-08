// Declare a variable named language without assigning any value
let language;

// Define a function named helloWorld that takes one parameter, language
function helloWorld(language) {
    // Check if the language is "jap"
    if (language == "jap") {
        // If true, log the Japanese translation of "Hello, World!" to the console
        console.log("魚を入れる");
    // Check if the language is "rus"
    } else if (language == "rus") {
        // If true, log the Russian translation of "Hello, World!" to the console
        console.log("рука на диване");
    // Check if the language is "ara"
    } else if (language == "ara") {
        // If true, log the Arabic translation of "Hello, World!" to the console
        console.log("نابولي");
    }
}

// Call the helloWorld function with different language codes
helloWorld("jap"); // Expected output: "魚を入れる"
helloWorld("rus"); // Expected output: "рука на диване"
helloWorld("ara"); // Expected output: "نابولي"