# Count 2D Array Element (Easy)

This problem requires you to count the number of elements equal to a given integer `k` in a 2D array of 32-bit integers, **without using any external libraries**.

## Problem Statement

Given:

- An input 2D array `input` of size `N x M` containing 32-bit integers
- An integer `k`

Count how many times the value `k` appears in the 2D array. The result must be stored in the variable `output`.

---

## Example

**Example 1:**

- Input:
  `input = [[1, 2, 3], [4, 5, 1]]`, `k = 1`
- Output:
  `output = 2`

**Example 2:**

- Input:
  `input = [[5, 10], [5, 2]]`, `k = 1`
- Output:
  `output = 0`

## Constraints

- 1 ≤ N, M ≤ 10,000
- 1 ≤ input[i], k ≤ 100
- No external libraries are allowed.
- The final result must be stored in the variable `output`.

## Solution

See [count_element_2d.py](./count_element_2d.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Count 2D Array Element](https://leetgpu.com/challenges/count-2d-array-element)
