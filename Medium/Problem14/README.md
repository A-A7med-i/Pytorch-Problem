# Ordinary Least Squares (Medium)

This problem requires you to solve the **Ordinary Least Squares (OLS) regression** problem on a GPU, **without using any external libraries**.

## Problem Statement

Given:

- A feature matrix **X** of size `n_samples × n_features`
- A target vector **y** of size `n_samples`

Compute the coefficient vector **beta** of size `n_features` that minimizes the sum of squared residuals:

```
minimize ||X * beta - y||^2
```

The closed-form solution to OLS is:

```
beta = (Xᵗ X)⁻¹ Xᵗ y
```

Assume that the feature matrix **X** is full rank (i.e., `Xᵗ X` is invertible).

## Example

*Note: Specific example values are not provided in the original problem statement.*

## Constraints

- 1 ≤ n_samples ≤ 100,000
- 1 ≤ n_features ≤ 1,000
- n_samples ≥ n_features
- -1000.0 ≤ values in X and y ≤ 1000.0
- Solutions are tested with absolute tolerance of 1e-2 and relative tolerance of 1e-2
- No external libraries are allowed.
- The final coefficients must be stored in the **beta** vector.

## Solution

See [ordinary_least_squares.py](./ordinary_least_squares.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Ordinary Least Squares](https://leetgpu.com/challenges/ordinary-least-squares)
