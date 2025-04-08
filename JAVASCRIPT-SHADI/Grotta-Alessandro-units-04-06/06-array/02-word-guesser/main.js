let word = ['P', 'O', 'L', 'T', 'E', 'R', 'G', 'U', 'Y', 'S'];
let guessedLetters = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'];
let maxGuesses = 6;
let remainingGuesses = maxGuesses;

function guessLetter(letter) {
    let correctGuess = false;
    for (let i = 0; i < word.length; i++) {
        if (word[i] === letter) {
            guessedLetters[i] = letter;
            correctGuess = true;
        }
    }
    if (correctGuess) {
        console.log(`Correct! The word now looks like this: ${guessedLetters.join(' ')}`);
    } else {
        remainingGuesses--;
        console.log(`Wrong guess. You have ${remainingGuesses} guesses left.`);
    }
    if (!guessedLetters.includes('_')) {
        console.log('Congratulations! You guessed the word!');
    } else if (remainingGuesses === 0) {
        console.log('Sorry, you lost. The word was ' + word.join(''));
    }
}

function startGame() {
    while (remainingGuesses > 0 && guessedLetters.includes('_')) {
        let userGuess = prompt('Guess a letter:').toUpperCase();
        guessLetter(userGuess);
    }
}

startGame();