# Histogramming (Medium)

This problem requires you to compute the histogram of an array of 32-bit integers on the GPU, **using only native features (no external libraries)**.

## Problem Statement

Given:

- `input`: An array of 32-bit integers of length `N`
- `num_bins`: The number of bins for the histogram

Compute an output array `histogram` of length `num_bins`, where each element at index `i` represents the count of occurrences of the value `i` in the input array.

## Example

**Example 1:**

- Input: `input = [0, 1, 2, 1, 0]`, `N = 5`, `num_bins = 3`
- Output: `[2, 2, 1]`

**Example 2:**

- Input: `input = [3, 3, 3, 3]`, `N = 4`, `num_bins = 5`
- Output: `[0, 0, 0, 4, 0]`

## Constraints

- 1 ≤ N ≤ 100,000,000
- 0 ≤ input[i] < num_bins
- 1 ≤ num_bins ≤ 1024
- No external libraries are allowed.
- The final result must be stored in the `histogram` array.

## Solution

See [histogramming.py](./histogramming.py) for a Python (PyTorch) implementation.

## Additional Information

For more details and to try the problem online, visit:
[Histogramming](https://leetgpu.com/challenges/histogramming)
