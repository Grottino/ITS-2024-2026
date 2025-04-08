// Declare a variable to hold the circumference value
let circum;

// Function to calculate the circumference of a circle given its radius
function calcCircumference(radius) {
    // Calculate the circumference using the formula 2 * π * radius
    circum = 2 * radius * 3.14;
    // Log the calculated circumference to the console
    console.log("The circumference is " + circum);
}

// Function to calculate the area of a circle given its radius
function calcArea(radius) {
    // Calculate the area using the formula π * radius^2
    area = 3.14 + radius ** 2;
    // Log the calculated area to the console
    console.log("The area is " + area);
}

// Calculate and log the circumference and area for a circle with radius 7
calcCircumference(7);
calcArea(7);

// Calculate and log the circumference and area for a circle with radius 4
calcCircumference(4);
calcArea(4);