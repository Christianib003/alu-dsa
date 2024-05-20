const fs = require("fs")

// import data from file
const data = fs.readFileSync("../../sample_inputs/sample_inputs.txt", "utf8")

// split data by new line
const lines = data.split("\n");

// create an object to store the count of valid numbers
const tally = {}

// loop through an array of strings. for each element...
for(let line of lines) {
    // trim the string
    const trimmedLine = trimString(line);

    // convert string to integer
    const num = convertStringToInt(trimmedLine);

    // check if interger is -1023 <= int >= 1023
    if(isInRange(num)) {
        // keep track of count of valid numbers
        trackCount(num, tally);
    }
}

// push the tally values into an array
const tallyArr = Object.values(tally);

// sort the array
const sortedArr = sortArr(tallyArr);

// write a new results file using data from the array
for(let num of sortedArr) {
    fs.appendFileSync("../../sample_results/sample_results.txt", num + "\n")
}

// create function to trim a string
function trimString(str) {
    // create a new string to store the trimmed string
    let newStr = "";

    // loop through the string
    for(let char of str) {
        // if the character is not a space, add it to the new string
        if(char !== " ") newStr += char;
    }
    return newStr;
}

// create function to convert a string to an integer
function convertStringToInt(str) {
    return parseInt(str);
}

// create function to check if a number is in valid range
function isInRange(num) {
    return num >= -1023 && num <= 1023;
}

// create function to keep track of count of valid numbers
function trackCount(num, obj) {
    // if the number is in the tally object, increment the count
    if(!obj[num]) obj[num] = num; // ex {"1": 1}"}
}

// use quick sort algorithm to sort the array
function sortArr(arr) {
    // if the array is empty or has only one element, return the array
    if (arr.length <= 1) {
        return arr;
    }
    // create a pivot point
    const pivot = arr[Math.floor(arr.length / 2)];
    const left = [];
    const right = [];

    // loop through the array
    for (let i = 0; i < arr.length; i++) {
        if (i !== Math.floor(arr.length / 2)) {
            if (arr[i] < pivot) {
                left.push(arr[i]);
            } else {
                right.push(arr[i]);
            }
        }
    }

    // recursively call quickSort on the left and right arrays
    return sortArr(left).concat(pivot, sortArr(right));
}
