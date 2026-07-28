// JS verification of TypedEmitter logic (compiled-style usage)
const { TypedEmitter } = require('./event_emitter.js');

class TypedEmitterJS extends TypedEmitter {}

const e = new TypedEmitterJS();
const calls = [];
e.on('click', (d) => calls.push(d.x));
const had = e.emit('click', { x: 10, y: 20 });
console.assert(had === true);
console.assert(calls[0] === 10);

const had2 = e.emit('close', undefined);
console.assert(had2 === false);

e.off('click', calls.length && (() => {}));
console.assert(e.listenerCount('click') === 1);  // we didn't actually pass the right fn — re-test

// Real off test
const h = (d) => calls.push(d.x);
e.on('click', h);
console.assert(e.listenerCount('click') === 2);
e.off('click', h);
console.assert(e.listenerCount('click') === 1);

// once
const onceCalls = [];
e.once('click', (d) => onceCalls.push(d.x));
console.assert(e.listenerCount('click') === 2);
e.emit('click', { x: 1, y: 0 });
e.emit('click', { x: 2, y: 0 });
console.assert(onceCalls.length === 1);
console.assert(onceCalls[0] === 1);
console.assert(e.listenerCount('click') === 1);

console.log("ALL TESTS PASSED");