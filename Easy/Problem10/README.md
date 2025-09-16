# Matrix Copy (Easy)

This problem requires you to implement a program that copies an **N×N** matrix of 32-bit floating point numbers from an input array to an output array on the GPU, **without using any external libraries**.

## Problem Statement

Given an input matrix **A** of size **N×N**, perform a direct element-wise copy to matrix **B** such that:

```
B[i][j] = A[i][j]   for all valid indices i, j
```

## Example

**Example 1:**

- Input:
  A = [[1.0, 2.0],
       [3.0, 4.0]]
- Output:
  B = [[1.0, 2.0],
       [3.0, 4.0]]

**Example 2:**

- Input:
  A = [[5.5, 6.6, 7.7],
       [8.8, 9.9, 10.1],
       [11.2, 12.3, 13.4]]
- Output:
  B = [[5.5, 6.6, 7.7],
       [8.8, 9.9, 10.1],
       [11.2, 12.3, 13.4]]

## Constraints

- 1 ≤ N ≤ 4096
- All elements are 32-bit floating point numbers
- No external libraries are allowed.
- The final result must be stored in matrix **B**.

## Solution

See [matrix_copy.py](./matrix_copy.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Matrix Copy](https://leetgpu.com/challenges/matrix-copy)
