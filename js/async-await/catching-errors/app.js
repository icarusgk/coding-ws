const cookBeanSouffle = require('./library.js');

// Write your code below:
async function hostDinnerParty() {
  try {
    const value = await cookBeanSouffle();
    console.log(`${value} is served!`);
  } catch (error) {
    console.log(error);
    console.log('Ordering a pizza!');
  }
}


hostDinnerParty();



