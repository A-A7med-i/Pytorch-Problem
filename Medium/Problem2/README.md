# 2D Convolution (Medium)

This problem requires you to implement a **2D convolution operation** on the GPU, using only native features (no external libraries).

## Problem Statement

Given:

- `input`: A 2D matrix of 32-bit floating-point numbers, represented as a 1D array in row-major order.
- `kernel`: A 2D kernel (filter) of 32-bit floating-point numbers, also as a 1D array in row-major order.

Compute the "valid" convolution, meaning the kernel is only applied where it fully overlaps with the input.
The output matrix (also a 1D array in row-major order) will have dimensions:

- `output_rows = input_rows - kernel_rows + 1`
- `output_cols = input_cols - kernel_cols + 1`

For each output element at position `(i, j)`:

```
output[i, j] = sum_{m=0}^{kernel_rows-1} sum_{n=0}^{kernel_cols-1} input[(i+m)*input_cols + (j+n)] * kernel[m*kernel_cols + n]
```

## Example

**Example 1:**

- Input:
  input (3×3):
  kernel (2×2):
  `input_rows = 3`, `input_cols = 3`
  `kernel_rows = 2`, `kernel_cols = 2`
- Output:
  output (2×2)

**Example 2:**

- Input:
  input (4×4):
  kernel (1×3):
  `input_rows = 4`, `input_cols = 4`
  `kernel_rows = 1`, `kernel_cols = 3`
- Output:
  output (4×2)

## Constraints

- 1 ≤ input_rows, input_cols ≤ 3072
- 1 ≤ kernel_rows, kernel_cols ≤ 31
- kernel_rows ≤ input_rows
- kernel_cols ≤ input_cols
- No external libraries are allowed.
- The final result must be stored in the array `output`.

## Solution

See [convolution_2d.py](./convolution_2d.py) for a Python (PyTorch) implementation.

## Additional Information

For more details and to try the problem online, visit:
[2D Convolution](https://leetgpu.com/challenges/2d-convolution)
