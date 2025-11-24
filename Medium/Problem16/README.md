# Matrix Power (Medium)

This problem requires you to raise a square matrix to an integer power on the GPU, **without using any external libraries**.

## Problem Statement

Given:

- `input`: A flattened square matrix of size `N × N` (row-major order)
- `output`: An empty output matrix of the same size (row-major order)
- `N`: The dimension of the matrix
- `P`: The exponent (integer power)

Compute:

```
output = input^P
```

where matrix multiplication is standard dense multiplication over 32-bit floating point numbers.

The final result must be written to the `output` array in row-major order.

## Example

**Example 1:**

- Input:

  ```
  input  = [[1.0, 2.0],
            [3.0, 4.0]]
  N      = 2
  P      = 3
  ```

- Output:

  ```
  output = [[37.0, 54.0],
            [81.0, 118.0]]
  ```

**Example 2:**

- Input:

  ```
  input  = [[1.0, 0.0, 2.0],
            [0.0, 1.0, 0.0],
            [3.0, 0.0, 0.0]]
  N      = 3
  P      = 2
  ```

- Output:

  ```
  output = [[7.0, 0.0, 2.0],
            [0.0, 1.0, 0.0],
            [3.0, 0.0, 6.0]]
  ```

## Constraints

- The input matrix is square (N × N)
- 1 ≤ N (no upper bound specified)
- P is a non-negative integer
- All elements are 32-bit floating point numbers
- No external libraries are permitted
- The final result must be written to the output array in row-major order

## Solution

See [matrix_power.py](./matrix_power.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Matrix Power](https://leetgpu.com/challenges/matrix-power)
