# Vector Addition (Easy)

This problem requires you to implement element-wise addition of two vectors containing 32-bit floating point numbers on a GPU, **without using any external libraries**.

## Problem Statement

Given two input vectors `A` and `B` of equal length, compute their element-wise sum and store the result in vector `C`.

- **Input:** Two vectors `A` and `B` of length `N` (1 ≤ N ≤ 100,000,000), each containing 32-bit floating point numbers.
- **Output:** A vector `C` of length `N` where `C[i] = A[i] + B[i]` for all valid indices `i`.

## Example

**Example 1:**

- Input:
  A = [1.0, 2.0, 3.0, 4.0]
  B = [5.0, 6.0, 7.0, 8.0]
- Output:
  C = [6.0, 8.0, 10.0, 12.0]

**Example 2:**

- Input:
  A = [1.5, 1.5, 1.5]
  B = [2.3, 2.3, 2.3]
- Output:
  C = [3.8, 3.8, 3.8]

## Constraints

- Input vectors `A` and `B` have identical lengths.
- No external libraries are allowed.
- The final result must be stored in vector `C`.

## Solution

See [vector_addition.py](./vector_addition.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Vector Addition](https://leetgpu.com/challenges/vector-addition)
