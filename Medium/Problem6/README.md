# Dot Product (Medium)

This problem requires you to compute the **dot product** of two vectors containing 32-bit floating point numbers using CUDA, **without using any external libraries**.

## Problem Statement

Given two input vectors `A` and `B` of identical length `N`, compute their dot product.
The dot product is defined as:

```
result = sum_{i=0}^{N-1} (A[i] * B[i])
```

The final result must be stored in the output variable.

## Example

**Example 1:**

- Input:
  `A = [1.0, 2.0, 3.0, 4.0]`
  `B = [5.0, 6.0, 7.0, 8.0]`
- Output:
  `result = 70.0`  (1.0*5.0 + 2.0*6.0 + 3.0*7.0 + 4.0*8.0)

**Example 2:**

- Input:
  `A = [0.5, 1.5, 2.5]`
  `B = [2.0, 3.0, 4.0]`
- Output:
  `result = 16.0`  (0.5*2.0 + 1.5*3.0 + 2.5*4.0)

## Constraints

- A and B have identical lengths
- 1 ≤ N ≤ 100,000,000
- Use only CUDA native features (no external libraries).
- The final result must be stored in the output variable.

## Solution

See [dot_product.py](./dot_product.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Dot Product](https://leetgpu.com/challenges/dot-product)
