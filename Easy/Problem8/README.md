# Leaky ReLU (Easy)

This problem requires you to implement the leaky ReLU activation function on a vector of floating-point numbers, **without using any external libraries**.

## Problem Statement

Given an input vector **`x`** of size **`N`**, apply the **Leaky ReLU** activation function element-wise to produce the output vector **`y`**.

The Leaky ReLU function is defined as:

$$
y_i =
\begin{cases}
x_i, & x_i \geq 0 \\
\alpha \, x_i, & x_i < 0
\end{cases}
$$

where `0.01` is the leaky coefficient.

---

## Example

**Example 1:**

- Input:  `x = [1.0, -2.0, 3.0, -4.0]`
- Output: `y = [1.0, -0.02, 3.0, -0.04]`

**Example 2:**

- Input:  `x = [-1.5, 0.0, 2.5, -3.0]`
- Output: `y = [-0.015, 0.0, 2.5, -0.03]`

## Constraints

- 1 ≤ N ≤ 100,000,000
- -1000.0 ≤ input[i] ≤ 1000.0
- No external libraries are allowed.
- The final result must be stored in the vector `output`.

## Solution

See [leaky_relu.py](./leaky_relu.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Leaky ReLU](https://leetgpu.com/challenges/leaky-relu)
