'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */

// Return true if character is vowel
function isVowel(a) {
    switch (a) {
        case 'a': case 'i' : case 'o' : case 'e' : case 'u':
            return true;
        default:
            return false;
    }
}

function vowelsAndConsonants(s) {
    var i;
    var vowels = "";
    var consonants = "";
    for ( i of s ) {
        if (isVowel(i) == 1) {
            vowels += i;
        }
        else {
            consonants += i;
        }
    }

    for ( i of vowels ) {
        console.log(i);
    }

    for ( i of consonants ) {
        console.log(i);
    }
}

function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
