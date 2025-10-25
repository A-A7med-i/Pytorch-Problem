# Reduction (Medium)

This problem requires you to perform a **parallel reduction** on an array of 32-bit floating point numbers using CUDA, **without using any external libraries**.

## Problem Statement

Given an input array of size `N`, compute the sum of all its elements using parallel reduction on the GPU. The result should be stored in the output variable.

## Example

**Example 1:**

- Input: `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]`
- Output: `36.0`

**Example 2:**

- Input: `[-2.5, 1.5, -1.0, 2.0]`
- Output: `0.0`

## Constraints

- 1 ≤ N ≤ 100,000,000
- -1000.0 ≤ input[i] ≤ 1000.0
- Use only CUDA native features (no external libraries).
- The final result must be stored in the output variable.

## Solution

See [reduction.py](./reduction.py) for a Python (PyTorch) implementation.

## Additional Information

For more details and to try the problem online, visit:
[Reduction](https://leetgpu.com/challenges/reduction)
