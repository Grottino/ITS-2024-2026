// Declare a variable to hold the age
let age;

// Declare a variable to hold the amount of coffee consumed per day
let amountPerDay;

// Function to calculate the total coffee supply needed until the age of 73
function calculateSupply(age, amountPerDay) {
    // Calculate the total amount of coffee needed
    amountPerDay = amountPerDay * (73 - age);
    // Log the calculated amount to the console
    console.log("You will need " + amountPerDay + " cups of coffee to last you until the age of 73");
}

// Calculate and log the coffee supply needed for a person aged 54 who drinks 1 cup per day
calculateSupply(54, 1);

// Calculate and log the coffee supply needed for a person aged 19 who drinks 4 cups per day
calculateSupply(19, 4);

// Calculate and log the coffee supply needed for a person aged 26 who drinks 2 cups per day
calculateSupply(26, 2);