// Token-bucket rate limiter — lazy refill using Date.now().

class RateLimiter {
  constructor({ capacity, refillRate, refillInterval }) {
    if (!(capacity > 0)) throw new Error("capacity must be > 0");
    if (!(refillRate > 0)) throw new Error("refillRate must be > 0");
    if (!(refillInterval > 0)) throw new Error("refillInterval must be > 0");
    this._capacity = capacity;
    this._refillRate = refillRate;
    this._refillInterval = refillInterval;
    this._tokens = capacity;
    this._lastRefill = Date.now();
  }

  _refill(now) {
    const elapsed = now - this._lastRefill;
    if (elapsed <= 0) return;
    const intervals = Math.floor(elapsed / this._refillInterval);
    if (intervals > 0) {
      this._tokens = Math.min(this._capacity, this._tokens + intervals * this._refillRate);
      this._lastRefill += intervals * this._refillInterval;
    }
  }

  available() {
    this._refill(Date.now());
    return Math.floor(this._tokens);
  }

  tryConsume(n = 1) {
    if (!(n > 0)) throw new Error("n must be > 0");
    this._refill(Date.now());
    if (this._tokens >= n) {
      this._tokens -= n;
      return true;
    }
    return false;
  }
}

module.exports = { RateLimiter };