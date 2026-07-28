// Exact BountyBook test for dep_resolver
import { DependencyResolver, CyclicDependencyError } from './dep_resolver.js';

const g1 = { a: [], b: ["a"], c: ["b"] };
const r1 = new DependencyResolver(g1);
const order1 = r1.resolve("c");
console.assert(order1.indexOf("a") < order1.indexOf("b"), "a before b");
console.assert(order1.indexOf("b") < order1.indexOf("c"), "b before c");
console.assert(order1.includes("a") && order1.includes("b") && order1.includes("c"), "all packages present");

const g2 = { a: [], b: ["a"], c: ["a"], d: ["b", "c"] };
const r2 = new DependencyResolver(g2);
const order2 = r2.resolve("d");
console.assert(order2.indexOf("a") < order2.indexOf("b"), "diamond: a before b");
console.assert(order2.indexOf("a") < order2.indexOf("c"), "diamond: a before c");
console.assert(order2.indexOf("b") < order2.indexOf("d"), "diamond: b before d");
console.assert(order2.indexOf("c") < order2.indexOf("d"), "diamond: c before d");
console.assert(new Set(order2).size === order2.length, "no duplicates in diamond");

const g3 = { a: ["b"], b: ["c"], c: ["a"] };
const r3 = new DependencyResolver(g3);
try {
  r3.resolve("a");
  console.assert(false, "should throw on cycle");
} catch (e) {
  console.assert(e instanceof CyclicDependencyError, `expected CyclicDependencyError, got ${e.constructor.name}`);
  console.assert(Array.isArray(e.cycle), "cycle property should be array");
  console.assert(e.cycle.length >= 3, `cycle too short: ${e.cycle}`);
}

const r3b = new DependencyResolver({ x: [] });
try {
  r3b.resolve("nonexistent");
  console.assert(false, "should throw on missing entry point");
} catch (e) {
  console.assert(!(e instanceof CyclicDependencyError), "should not be cyclic error");
}

const g4 = { a: [], b: ["a"], c: ["a"], d: [] };
const r4 = new DependencyResolver(g4);
const all = r4.resolveAll();
console.assert(all.length === 4, `expected 4, got ${all.length}`);
console.assert(all.indexOf("a") < all.indexOf("b"), "a before b in resolveAll");
console.assert(new Set(all).size === all.length, "no duplicates in resolveAll");

console.log("ALL TESTS PASSED");