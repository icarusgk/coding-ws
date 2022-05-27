const express = require('express');

const app = express();
const PORT = 4001;

app.listen(PORT, () => {
  console.log(`Listening on port: ${PORT}`);
})



app.get('/expressions', (req, res, next) => {
  console.log(req);
  
})