# ReLU (Rectified Linear Unit) (Easy)

This problem requires you to implement the Rectified Linear Unit (ReLU) activation function on a vector of 32-bit floating point numbers, **without using any external libraries**.

## Problem Statement

Given an input vector of size `N`, apply the ReLU function to each element and store the result in the output vector.
The ReLU function is defined as:

```
ReLU(x) = max(0, x)
```

## Example

**Example 1:**

- Input:  `input = [-2.0, -1.0, 0.0, 1.0, 2.0]`
- Output: `output = [0.0, 0.0, 0.0, 1.0, 2.0]`

**Example 2:**

- Input:  `input = [-3.5, 0.0, 4.2]`
- Output: `output = [0.0, 0.0, 4.2]`

## Constraints

- 1 ≤ N ≤ 100,000,000
- No external libraries are allowed.
- The final result must be stored in `output`.

## Solution

See [relu.py](./relu.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[ReLU](https://leetgpu.com/challenges/relu)
