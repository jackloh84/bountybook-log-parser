// PubSub class — exact + wildcard (* = single segment, # = multi-segment) topic patterns.
// No external packages.

export class PubSub {
  constructor() {
    this._handlers = []; // [{pattern, handler, id}]
    this._nextId = 1;
  }

  subscribe(pattern, handler) {
    const id = this._nextId++;
    const entry = { pattern, handler, id };
    this._handlers.push(entry);
    return () => {
      const idx = this._handlers.indexOf(entry);
      if (idx >= 0) this._handlers.splice(idx, 1);
    };
  }

  publish(topic, message) {
    let count = 0;
    for (const { pattern, handler } of this._handlers) {
      if (this._match(pattern, topic)) {
        try { handler(topic, message); } catch { /* swallow handler errors */ }
        count++;
      }
    }
    return count;
  }

  subscriberCount(pattern) {
    let n = 0;
    for (const { pattern: p } of this._handlers) {
      if (p === pattern) n++;
    }
    return n;
  }

  _match(pattern, topic) {
    if (pattern === topic) return true;
    if (!pattern.includes("*") && !pattern.includes("#")) return false;
    const pSegs = pattern.split(".");
    const tSegs = topic.split(".");
    let pi = 0, ti = 0;
    while (pi < pSegs.length && ti < tSegs.length) {
      const p = pSegs[pi];
      if (p === "#") {
        // # matches one or more remaining segments; consume to end
        return true;
      }
      if (p === "*" || p === tSegs[ti]) {
        pi++; ti++;
      } else {
        return false;
      }
    }
    // After-loop cases:
    // - pattern fully consumed
    // - remaining pattern is just "#" (matches empty remainder)
    while (pi < pSegs.length) {
      if (pSegs[pi] === "#") { pi++; continue; }
      return false;
    }
    return pi === pSegs.length && ti === tSegs.length;
  }
}