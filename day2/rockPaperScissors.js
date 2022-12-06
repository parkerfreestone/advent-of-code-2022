const fs = require("fs");

const determineOutcome = (round) => {
    
}

const fileContents = fs.readFileSync("./input.txt", "utf-8");

fileContents
  .trim()
  .split("\n")
  .forEach((round) => {
    console.log(round[0] === "A");
  });
