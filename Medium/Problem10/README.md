# Mean Squared Error (Medium)

This problem requires you to calculate the **Mean Squared Error (MSE)** between two arrays of 32-bit floating point numbers using CUDA, **without using any external libraries**.

## Problem Statement

Given two arrays of equal length:

- `predictions`: An array of predicted values
- `targets`: An array of target (ground truth) values

Compute the mean squared error (MSE) as:

```
mse = (1/N) * sum_{i=0}^{N-1} (predictions[i] - targets[i])^2
```

where `N` is the number of elements in each array.

The final result must be stored in the variable `mse`.

## Example

**Example 1:**

- Input:
  `predictions = [1.0, 2.0, 3.0, 4.0]`
  `targets = [1.5, 2.5, 3.5, 4.5]`
- Output:
  `mse = 0.25`

**Example 2:**

- Input:
  `predictions = [10.0, 20.0, 30.0]`
  `targets = [12.0, 18.0, 33.0]`
- Output:
  `mse = 5.67`

## Constraints

- 1 ≤ N ≤ 100,000,000
- -1000.0 ≤ predictions[i], targets[i] ≤ 1000.0
- No external libraries are allowed.
- The final result must be stored in the `mse` variable.

## Solution

See [mean_squared_error.py](./mean_squared_error.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Mean Squared Error](https://leetgpu.com/challenges/mean-squared-error)
