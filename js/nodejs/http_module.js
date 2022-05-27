const http = require('http');

const server = http.createServer((res, req) => {
  res.on("Server is listening!");
});

server.listen(8080, () => {
  
})