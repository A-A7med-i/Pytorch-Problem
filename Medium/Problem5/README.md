# Prefix Sum (Medium)

This problem requires you to compute the **prefix sum (cumulative sum)** of an array of 32-bit floating point numbers using CUDA, **without using any external libraries**.

## Problem Statement

Given an input array of size `N`, compute the prefix sum (also known as the cumulative sum), where each element at index `i` in the output array is the sum of all elements from index `0` to `i` in the input array.

For example, for input `[a, b, c, d, ...]`, the prefix sum is `[a, a+b, a+b+c, a+b+c+d, ...]`.

The result must be stored in the output array.

## Example

**Example 1:**

- Input: `[1.0, 2.0, 3.0, 4.0]`
- Output: `[1.0, 3.0, 6.0, 10.0]`

**Example 2:**

- Input: `[5.0, -2.0, 3.0, 1.0, -4.0]`
- Output: `[5.0, 3.0, 6.0, 7.0, 3.0]`

## Constraints

- 1 ≤ N ≤ 100,000,000
- -1000.0 ≤ input[i] ≤ 1000.0
- The largest value in the output array will fit within a 32-bit float
- Use only CUDA native features (no external libraries).
- The result must be stored in the output array.

## Solution

See [prefix_sum.py](./prefix_sum.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Prefix Sum](https://leetgpu.com/challenges/prefix-sum)
