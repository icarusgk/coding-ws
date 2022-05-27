process.stdout.write("I'm thinking of a number from 1 through 10. What do you think it is? \n(Write \"quit\" to give up.)\n\nIs the number ... ");

let playGame = (userInput) => {
  let input = userInput.toString().trim();
  if (input === "1") {
    console.log("Correct!", input);
    process.exit();
  } else {
    console.log("wrong!");
  }
};

process.stdin.on('data', playGame);

