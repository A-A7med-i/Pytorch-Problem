# Gaussian Blur (Medium)

This problem requires you to apply a **Gaussian blur filter** to a 2D image using convolution, **without using any external libraries**.

## Problem Statement

Given:

- An input image as a 2D floating-point array (row-major order)
- A Gaussian kernel as a 2D floating-point array (row-major order)

Compute the convolution of the image with the kernel. For each output pixel at position `(i, j)`, the value is calculated as the weighted sum of its neighbors, where the weights are given by the Gaussian kernel.
**Boundary conditions:** Use zero-padding (treat values outside the image boundary as zeros).

The final result must be stored in the output array.

## Example

**Example 1:**

- Input:
  image (5×5):

  ```
  [
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [6.0, 7.0, 8.0, 9.0, 10.0],
    [11.0, 12.0, 13.0, 14.0, 15.0],
    [16.0, 17.0, 18.0, 19.0, 20.0],
    [21.0, 22.0, 23.0, 24.0, 25.0]
  ]
  ```

  kernel (3×3):

  ```
  [
    [0.0625, 0.125, 0.0625],
    [0.125, 0.25, 0.125],
    [0.0625, 0.125, 0.0625]
  ]
  ```

- Output:
  output (5×5):

  ```
  [
    [1.6875, 2.75, 3.5, 4.25, 3.5625],
    [4.75, 7.0, 8.0, 9.0, 7.25],
    [8.5, 12.0, 13.0, 14.0, 11.0],
    [12.25, 17.0, 18.0, 19.0, 14.75],
    [11.0625, 15.25, 16.0, 16.75, 12.9375]
  ]
  ```

**Example 2:**

- Input:
  image (3×3):

  ```
  [
    [10.0, 20.0, 30.0],
    [40.0, 50.0, 60.0],
    [70.0, 80.0, 90.0]
  ]
  ```

  kernel (3×3):

  ```
  [
    [0.1, 0.1, 0.1],
    [0.1, 0.2, 0.1],
    [0.1, 0.1, 0.1]
  ]
  ```

- Output:
  output (3×3):

  ```
  [
    [13.0, 23.0, 19.0],
    [31.0, 50.0, 39.0],
    [31.0, 47.0, 37.0]
  ]
  ```

## Constraints

- 1 ≤ input_rows, input_cols ≤ 4096
- 3 ≤ kernel_rows, kernel_cols ≤ 21 (both odd)
- All kernel values are non-negative and sum to 1.0 (normalized)
- Use zero-padding for boundaries
- No external libraries are allowed
- The final result must be stored in the output array

## Solution

See [gaussian_blur.py](./gaussian_blur.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Gaussian Blur](https://leetgpu.com/challenges/gaussian-blur)
