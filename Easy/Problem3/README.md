# Matrix Transpose (Easy)

This problem requires you to implement the transpose of a matrix containing 32-bit floating point numbers on a GPU, **without using any external libraries**.

## Problem Statement

Given a matrix `A` of dimensions `rows × cols`, compute its transpose `output` of dimensions `cols × rows`, where the element at position `(i, j)` in `A` becomes the element at position `(j, i)` in `output`. All matrices are stored in row-major format.

## Example

**Example 1:**

- Input: 2×3 matrix
  [ [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0] ]
- Output: 3×2 matrix
  [ [1.0, 4.0],
    [2.0, 5.0],
    [3.0, 6.0] ]

**Example 2:**

- Input: 3×1 matrix
  [ [7.0],
    [8.0],
    [9.0] ]
- Output: 1×3 matrix
  [ [7.0, 8.0, 9.0] ]

## Constraints

- 1 ≤ rows, cols ≤ 8192
- Input matrix dimensions: rows × cols
- Output matrix dimensions: cols × rows
- No external libraries are allowed.
- The final result must be stored in the matrix `output`.

## Solution

See [matrix_transpose.py](./matrix_multiplication.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Matrix Transpose](https://leetgpu.com/challenges/matrix-transpose)
