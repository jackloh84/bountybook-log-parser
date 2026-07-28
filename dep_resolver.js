// Dependency resolver with cycle detection (DFS grey/black coloring).

export class CyclicDependencyError extends Error {
  constructor(cycle) {
    super(`Cyclic dependency detected: ${cycle.join(" -> ")}`);
    this.name = "CyclicDependencyError";
    this.cycle = cycle;
  }
}

export class DependencyResolver {
  constructor(graph) {
    this._graph = graph || {};
  }

  resolve(entryPoint) {
    if (!(entryPoint in this._graph)) {
      throw new Error(`Entry point '${entryPoint}' not in graph`);
    }
    const order = [];
    const visited = new Set();   // black: fully processed
    const onStack = new Map();   // grey: currently on DFS stack, value = parent

    const visit = (node, path) => {
      if (visited.has(node)) return;
      if (onStack.has(node)) {
        // cycle: slice path from first occurrence of node
        const idx = path.indexOf(node);
        const cycle = idx >= 0 ? [...path.slice(idx), node] : [...path, node];
        throw new CyclicDependencyError(cycle);
      }
      onStack.set(node, true);
      const deps = this._graph[node] || [];
      for (const dep of deps) {
        visit(dep, [...path, node]);
      }
      onStack.delete(node);
      visited.add(node);
      order.push(node);
    };

    visit(entryPoint, []);
    return order;
  }

  resolveAll() {
    const order = [];
    const visited = new Set();
    const onStack = new Map();

    const visit = (node, path) => {
      if (visited.has(node)) return;
      if (onStack.has(node)) {
        const idx = path.indexOf(node);
        const cycle = idx >= 0 ? [...path.slice(idx), node] : [...path, node];
        throw new CyclicDependencyError(cycle);
      }
      onStack.set(node, true);
      const deps = this._graph[node] || [];
      for (const dep of deps) {
        visit(dep, [...path, node]);
      }
      onStack.delete(node);
      visited.add(node);
      order.push(node);
    };

    for (const node of Object.keys(this._graph)) {
      visit(node, []);
    }
    return order;
  }
}