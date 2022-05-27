const http = require('http');

// Creates server instance
const server = http.createServer((req, res) => {
  const { method } = req;

  switch (method) {
    case 'GET':
      return handleGetRequest(req, res);
    default:
      throw new Error(`Unsupported request method: ${method}`);
  }

});

const handleGetRequest = (req, res) => {
  const pathname = req.url;

  if (pathname === '/users') {
    let data = [];
    return res.end(JSON.stringify(data));
  }

  res.statusCode = 404;
  return res.end('Requested resource does not exist');
}

// Starts server listening on specified port
server.listen(4001, () => {
  const { address, port } = server.address();
  console.log(`Server is listening on: http://${address}:${port}`);
});