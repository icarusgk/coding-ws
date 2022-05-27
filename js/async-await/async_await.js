function shopForBeans() {
  return new Promise((resolve, reject) => {
    const beanTypes = ['kidney', 'fava', 'pinto', 'black'];;

    setTimeout(() => {
      let randomIndex = Math.floor(Math.random() * 3);
      let beanType = beanTypes[randomIndex];

      console.log(`2. I bought ${beanType} beans because they were on sale.`)
      resolve(beanType);
    }, 1000);
  })
}

function getBeansNoAwait() {
  console.log("1. Heading to the store to buy beans.");
  let value = shopForBeans();
  console.log(`3. Great! I'm making ${value} beans for tonight!`);
}


async function getBeans() {
  console.log("1. Heading to the store to buy beans.");
  let value = await shopForBeans();
  console.log(`3. Great! I'm making ${value} beans for tonight!`);
}


getBeans();