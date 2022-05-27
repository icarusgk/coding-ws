let events = require('events')

let myEmitter = new events.EventEmitter();

myEmitter.on("celebrate", data => {
  console.log("Celebrate", data);
});

let festivities = ["Halloween", "Valentines", "Christmas"];

for (let i in festivities) {
  myEmitter.emit("celebrate", festivities[i]);
}

myEmitter.emit("celebrate", "this is a new emittion!!!");