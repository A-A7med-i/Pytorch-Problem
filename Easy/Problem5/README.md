# 1D Convolution (Easy)

This problem requires you to implement a 1D convolution operation on an input array using a given kernel (filter), **without using any external libraries**.

## Problem Statement

Given:

- `input`: A 1D array of 32-bit floating-point numbers.
- `kernel`: A 1D array of 32-bit floating-point numbers representing the convolution kernel.

Compute the "valid" convolution, meaning the kernel is only applied where it fully overlaps with the input. The output array will have a size of `input_size - kernel_size + 1`.

For each output element at index `i`:

```
output[i] = sum_{j=0}^{kernel_size-1} input[i + j] * kernel[j]
```

## Example

**Example 1:**

- Input:
  `input = [1, 2, 3, 4, 5]`
  `kernel = [1, 0, -1]`
- Output:
  `[-2, -2, -2]`

**Example 2:**

- Input:
  `input = [2, 4, 6, 8]`
  `kernel = [0.5, 0.2]`
- Output:
  `[1.8, 3.2, 4.6]`

## Constraints

- 1 ≤ input_size ≤ 1,500,000
- 1 ≤ kernel_size ≤ 2047
- kernel_size ≤ input_size
- No external libraries are allowed.
- The final result must be stored in the array `output`.

## Solution

See [convolution1d.py](./convolution1d.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[1D Convolution](https://leetgpu.com/challenges/1d-convolution)
