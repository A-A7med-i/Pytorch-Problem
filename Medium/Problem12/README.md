# Top K Selection (Medium)

This problem requires you to select the **k largest elements** from a 1D array of 32-bit floating point numbers on the GPU, **without using any external libraries**.

## Problem Statement

Given:

- `input`: A 1D array of 32-bit floating point numbers of length `N`
- `k`: The number of largest elements to select

Select the `k` largest elements from the input array and write them in **descending order** to the output array of length `k`.

## Example

**Example 1:**

- Input:
  `input = [1.0, 5.0, 3.0, 2.0, 4.0]`, `N = 5`, `k = 3`
- Output:
  `output = [5.0, 4.0, 3.0]`

**Example 2:**

- Input:
  `input = [7.2, -1.0, 3.3, 8.8, 2.2]`, `N = 5`, `k = 2`
- Output:
  `output = [8.8, 7.2]`

## Constraints

- 1 ≤ N ≤ 100,000,000
- 1 ≤ k ≤ N
- All values in input are 32-bit floats
- No external libraries are allowed.
- The final result must be stored in the output array.

## Solution

See [topk_selection.py](./topk_selection.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Top K Selection](https://leetgpu.com/challenges/top-k-selection)
