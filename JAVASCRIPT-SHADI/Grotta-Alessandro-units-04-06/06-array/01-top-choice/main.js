// Array of top choices
const topChoices = ["torquese", "cat", "Percy Jeckson", "Resident Evil"];

// Function to get the correct suffix
function getSuffix(number) {
    const suffixes = ["th", "st", "nd", "rd"];
    const value = number % 100;
    return suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0];
}

// Loop through the array and log the choices
topChoices.forEach((choice, index) => {
    const position = index + 1;
    const suffix = getSuffix(position);
    console.log(`My ${position}${suffix} choice is ${choice}.`);
});