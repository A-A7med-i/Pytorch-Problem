# Matrix Multiplication (Easy)

This problem requires you to implement matrix multiplication of two matrices containing 32-bit floating point numbers on a GPU, **without using any external libraries**.

## Problem Statement

Given two matrices `A` (of size M×K) and `B` (of size K×N), compute their matrix product `C` (of size M×N), where:

- `C[i][j] = sum(A[i][k] * B[k][j])` for all valid indices `i`, `j`, and `k`.
- All matrices are stored in row-major format.

## Example

**Example 1:**

- Input:
  Matrix A (2×3):
  [ [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0] ]
  Matrix B (3×2):
  [ [7.0, 8.0],
    [9.0, 10.0],
    [11.0, 12.0] ]
- Output:
  Matrix C (2×2):
  [ [58.0, 64.0],
    [139.0, 154.0] ]

**Example 2:**

- Input:
  Matrix A (1×2): [ [2.0, 3.0] ]
  Matrix B (2×1): [ [4.0], [5.0] ]
- Output:
  Matrix C (1×1): [ [23.0] ]

## Constraints

- 1 ≤ M, N, K ≤ 8192
- Input matrices are stored in row-major format.
- No external libraries are allowed.
- The final result must be stored in matrix `C`.
- Performance is measured with M = 8192, N = 6144, K = 4096.

## Solution

See [matrix_multiplication.p](./matrix_multiplication.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Matrix Multiplication](https://leetgpu.com/challenges/matrix-multiplication)
