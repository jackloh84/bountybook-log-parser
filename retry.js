// retry(fn, opts) — exponential backoff with optional jitter.
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function retry(fn, options = {}) {
  const maxAttempts = options.maxAttempts ?? 3;
  const baseDelayMs = options.baseDelayMs ?? 100;
  const factor = options.factor ?? 2;
  const jitter = options.jitter ?? false;

  let lastErr;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastErr = err;
      if (attempt >= maxAttempts) break;
      let delay = baseDelayMs * Math.pow(factor, attempt - 1);
      if (jitter) {
        delay = delay * (0.5 + Math.random());  // [0.5, 1.5)
      }
      await sleep(delay);
    }
  }
  throw lastErr;
}

module.exports = { retry };