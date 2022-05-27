function callback(error, user) {
  if (error) {
    console.error(error.message);
    return
    // process.exit(1);
  }

  console.log(`User with id: ${user.id} found! Their nickname is: ${user.nickname}`)
}

function getUser(id, callback) {
  return setTimeout(() => {
    if (id === 5) {
      callback(null, { id: id, nickname: "Teddy" });
    } else {
      // A second argument for user is not necessary since 
      // the function will end in the case of an error
      callback(new Error(`User with id: ${id} not found`));
    }
  }, 1000);
};




getUser(1, callback);
getUser(5, callback);

// * This is were the promisify function from the util module comes in play
const util = require('util');

const getUserPromise = util.promisify(getUser);

getUserPromise(5)
  .then((user) => {
    console.log(`User found! Their nickname is: ${user.nickname}`);
  })
  .catch((error) => {
    console.log('User not found', error);
  });

const user = async () => {
  try {
    let response = await getUserPromise(1);
    console.log(response);
  } catch (err) {
    console.log("ERRRORRRR!: ", err);
  }
}

user();
