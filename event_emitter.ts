// TypedEmitter<Events> with on/off/once/emit/listenerCount.
// No external dependencies.

type Listener<T> = (data: T) => void;

export class TypedEmitter<Events extends Record<string, unknown>> {
  private _listeners: Map<keyof Events, Listener<unknown>[]> = new Map();

  on<K extends keyof Events>(event: K, listener: Listener<Events[K]>): this {
    const list = this._listeners.get(event) || [];
    list.push(listener as Listener<unknown>);
    this._listeners.set(event, list);
    return this;
  }

  off<K extends keyof Events>(event: K, listener: Listener<Events[K]>): this {
    const list = this._listeners.get(event);
    if (!list) return this;
    const idx = list.indexOf(listener as Listener<unknown>);
    if (idx >= 0) list.splice(idx, 1);
    return this;
  }

  once<K extends keyof Events>(event: K, listener: Listener<Events[K]>): this {
    const wrapper: Listener<Events[K]> = (data) => {
      this.off(event, wrapper);
      listener(data);
    };
    return this.on(event, wrapper);
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): boolean {
    const list = this._listeners.get(event);
    if (!list || list.length === 0) return false;
    // Snapshot to allow mutations during emit (off/once auto-remove)
    const snapshot = list.slice();
    for (const fn of snapshot) {
      try { (fn as Listener<Events[K]>)(data); } catch { /* swallow */ }
    }
    return true;
  }

  listenerCount<K extends keyof Events>(event: K): number {
    return (this._listeners.get(event) || []).length;
  }
}