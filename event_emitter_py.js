// EventEmitter with on/once/emit/off/listenerCount/removeAllListeners. No deps.

class EventEmitter {
  constructor() {
    this._listeners = Object.create(null); // { event: [fn, ...] }
  }

  on(event, fn) {
    (this._listeners[event] || (this._listeners[event] = [])).push(fn);
    return this;
  }

  once(event, fn) {
    const wrapper = (...args) => {
      this.off(event, wrapper);
      fn(...args);
    };
    wrapper.__original = fn;
    return this.on(event, wrapper);
  }

  emit(event, ...args) {
    const list = this._listeners[event];
    if (!list || list.length === 0) return false;
    const snapshot = list.slice();
    for (const fn of snapshot) {
      try { fn(...args); } catch (_e) { /* swallow handler errors */ }
    }
    return true;
  }

  off(event, fn) {
    const list = this._listeners[event];
    if (!list) return this;
    // Allow removal by reference, or by wrapped once-handler whose original matches.
    for (let i = list.length - 1; i >= 0; i--) {
      const entry = list[i];
      if (entry === fn || (entry.__original && entry.__original === fn)) {
        list.splice(i, 1);
      }
    }
    return this;
  }

  listenerCount(event) {
    const list = this._listeners[event];
    return list ? list.length : 0;
  }

  removeAllListeners(event) {
    if (event === undefined) {
      this._listeners = Object.create(null);
    } else {
      delete this._listeners[event];
    }
    return this;
  }
}

module.exports = { EventEmitter };