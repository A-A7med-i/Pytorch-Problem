# Batched Matrix Multiplication (Medium)

This problem requires you to implement **batched matrix multiplication** in FP32 (32-bit floating point), **without using any external libraries**.

## Problem Statement

Given:

- A batch of matrices **A** of shape `[B, M, K]`
- A batch of matrices **B** of shape `[B, K, N]`

Compute the output batch **C** of shape `[B, M, N]` such that for each batch index `b`,
`C[b] = A[b] @ B[b]` (matrix multiplication for each batch).

All matrices are stored in row-major order and use 32-bit floating point numbers (FP32).

## Example

**Example 1:**

- Input:
  `B = 2, M = 2, K = 3, N = 2`
  `A = [`

  ```
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
    [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
  ]`
  `B = [`
  ```

    [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    [[6.0, 5.0], [4.0, 3.0], [2.0, 1.0]]
  ]`
- Output:
  `C = [`

  ```
    [[22.0, 28.0], [49.0, 64.0]],
    [[92.0, 68.0], [128.0, 95.0]]
  ]`

## Constraints

- 1 ≤ B ≤ 128
- 1 ≤ M, N, K ≤ 102
- No external libraries are allowed.
- The final result must be stored in the **C** array.

## Solution

See [batched_matrix_multiplication.py](./batched_matrix_multiplication.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Batched Matrix Multiplication](https://leetgpu.com/challenges/batched-matrix-multiplication)
