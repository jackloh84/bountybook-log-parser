// Exact copy of BountyBook verification test
import { PubSub } from './pubsub.js';

const ps = new PubSub();
const received = [];

const unsub1 = ps.subscribe("user.login", (t, m) => received.push([t, m]));
let count = ps.publish("user.login", { userId: 1 });
console.assert(count === 1, `publish should hit 1 handler, got ${count}`);
ps.publish("user.logout", { userId: 1 });
console.assert(received.length === 1, "only user.login should match");

const unsub2 = ps.subscribe("order.*", (t, m) => received.push([t, m]));
ps.publish("order.created", { id: 42 });
ps.publish("order.updated", { id: 42 });
ps.publish("order.item.added", { id: 42 });

const unsub3 = ps.subscribe("log.#", (t, m) => received.push([t, m]));
ps.publish("log.error", "crash");
ps.publish("log.db.query.slow", "slow query");

console.assert(received.length === 5, `expected 5, got ${received.length}`);

unsub1();
received.length = 0;
ps.publish("user.login", "x");
console.assert(received.length === 0, "unsubscribe should work");

console.assert(ps.subscriberCount("order.*") === 1, "order.* should have 1 sub");
console.assert(ps.subscriberCount("log.#") === 1, "log.# should have 1 sub");
unsub2();
console.assert(ps.subscriberCount("order.*") === 0, "order.* should have 0 subs after unsub");

unsub3();
const finalCount = ps.publish("anything", "hi");
console.assert(finalCount === 0, "no handlers, count should be 0");

console.log("ALL TESTS PASSED");