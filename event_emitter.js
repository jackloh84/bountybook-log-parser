"use strict";
// TypedEmitter<Events> with on/off/once/emit/listenerCount.
// No external dependencies.
Object.defineProperty(exports, "__esModule", { value: true });
exports.TypedEmitter = void 0;
class TypedEmitter {
    constructor() {
        this._listeners = new Map();
    }
    on(event, listener) {
        const list = this._listeners.get(event) || [];
        list.push(listener);
        this._listeners.set(event, list);
        return this;
    }
    off(event, listener) {
        const list = this._listeners.get(event);
        if (!list)
            return this;
        const idx = list.indexOf(listener);
        if (idx >= 0)
            list.splice(idx, 1);
        return this;
    }
    once(event, listener) {
        const wrapper = (data) => {
            this.off(event, wrapper);
            listener(data);
        };
        return this.on(event, wrapper);
    }
    emit(event, data) {
        const list = this._listeners.get(event);
        if (!list || list.length === 0)
            return false;
        // Snapshot to allow mutations during emit (off/once auto-remove)
        const snapshot = list.slice();
        for (const fn of snapshot) {
            try {
                fn(data);
            }
            catch { /* swallow */ }
        }
        return true;
    }
    listenerCount(event) {
        return (this._listeners.get(event) || []).length;
    }
}
exports.TypedEmitter = TypedEmitter;
