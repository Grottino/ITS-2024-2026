// Declare a variable to hold the number of children
let numChild;

// Declare a variable to hold the first name
let name1;

// Declare a variable to hold the second name
let name2;

// Declare a variable to hold the geographic location
let geoLoc;

// Declare a variable to hold the job title
let jobTitle;

// Function to tell fortune based on the provided parameters
function tellFortune(numChild, name2, geoLoc, jobTitle) {
    // Log the fortune message to the console
    console.log("You will be a " + jobTitle + " in " + geoLoc + ", and married to " + name2 + " with " + numChild + " kids.");
}

// Call the function with different sets of arguments and log the results
tellFortune(2, "Bionda", "Broklyn", "Singer");
tellFortune(4, "Dua Lipa", "Los Angeles", "Singer");
tellFortune(3, "Gwen Stacy", "NewYork", "Singer");