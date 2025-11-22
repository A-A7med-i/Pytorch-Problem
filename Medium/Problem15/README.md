# Monte Carlo Integration (Medium)

This problem requires you to implement **Monte Carlo integration** on a GPU, **without using any external libraries**.

## Problem Statement

Given:

- `y_samples`: A tensor of function values sampled at random points uniformly distributed in the interval `[a, b]`
- `a`, `b`: The integration interval
- `n_samples`: The number of samples

Estimate the definite integral:

```
∫ₐᵇ f(x) dx ≈ (b - a) * mean(y_samples)
```

The Monte Carlo method approximates the integral by computing the average of the function values and multiplying by the interval width.

The final result must be stored in the `result` variable.

## Example

- Input:
  `a = 0`, `b = 2`, `n_samples = 8`
  `y_samples = [0.0625, 0.25, 0.5625, 1.0, 1.5625, 2.25, 3.0625, 4.0]`
- Output:
  `result = 3.1875`

## Constraints

- 1 ≤ n_samples ≤ 100,000,000
- -1000.0 ≤ a < b ≤ 1000.0
- -10000.0 ≤ function values ≤ 10000.0
- The solution is tested with absolute tolerance of 1e-2 and relative tolerance of 1e-2

## Solution

See [monte_carlo_integration.py](./monte_carlo_integration.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Monte Carlo Integration](https://leetgpu.com/challenges/monte-carlo-integration)
