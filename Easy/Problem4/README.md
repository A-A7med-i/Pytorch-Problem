# Color Inversion (Easy)

This problem requires you to invert the colors of an image represented as a 1D array of RGBA values, using GPU programming **without any external libraries**.

## Problem Statement

Given an image as a 1D array `image` of size `width * height * 4`, where each pixel is represented by 4 consecutive 8-bit unsigned integers (R, G, B, A), invert the color of each pixel:

- For each pixel, set:
  - `R = 255 - R`
  - `G = 255 - G`
  - `B = 255 - B`
  - `A` remains unchanged

The result must be stored in the same `image` array.

## Example

**Example 1:**

- Input:
  `image = [255, 0, 128, 255, 0, 255, 0, 255]`, `width = 1`, `height = 2`
- Output:
  `[0, 255, 127, 255, 255, 0, 255, 255]`

**Example 2:**

- Input:
  `image = [10, 20, 30, 255, 100, 150, 200, 255]`, `width = 2`, `height = 1`
- Output:
  `[245, 235, 225, 255, 155, 105, 55, 255]`

## Constraints

- 1 ≤ width ≤ 4096
- 1 ≤ height ≤ 4096
- width * height ≤ 8,388,608
- No external libraries are allowed.
- The final result must be stored in the array `image`.

## Solution

See [color_inversion.py](./color_inversion.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Color Inversion](https://leetgpu.com/challenges/color-inversion)
