# Rainbow Table (Easy)

This problem requires you to perform **R rounds of parallel hashing** on an array of 32-bit integers using a provided hash function, **without using any external libraries**.

## Problem Statement

Given:

- `numbers`: An array of 32-bit integers of size `N`
- `R`: The number of hashing rounds

Apply the hash function to each element in the array for `R` rounds, where the output of one round becomes the input to the next. The final result must be stored in the array `output`.

## Example

**Example 1:**

- Input:
  `numbers = [123, 456, 789]`, `R = 2`
- Output:
  `hashes = [1636807824, 1273011621, 2193987222]`

**Example 2:**

- Input:
  `numbers = [0, 1, 2147483647]`, `R = 3`
- Output:
  `hashes = [96754810, 3571711400, 2006156166]`

## Constraints

- 1 ≤ N ≤ 10,000,000
- 1 ≤ R ≤ 100
- 0 ≤ input[i] ≤ 2,147,483,647
- No external libraries are allowed.
- The final result must be stored in the array `output`.

## Solution

See [rainbow_table.py](./rainbow_table.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Rainbow Table](https://leetgpu.com/challenges/rainbow-table)
