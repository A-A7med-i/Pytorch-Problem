# Sparse Matrix-Vector Multiplication (Medium)

This problem requires you to implement **sparse matrix-vector multiplication** using CUDA, **without using any external libraries**.

## Problem Statement

Given:

- A sparse matrix **A** of dimensions `M × N` (stored in row-major order, with `nnz` non-zero elements)
- A dense vector **x** of length `N`

Compute the product vector **y** of length `M`:

```
y = A @ x
```

where each element of `y` is the dot product of the corresponding row of `A` and the vector `x`.

The matrix **A** is approximately 60-70% sparse (i.e., 60-70% of its elements are zero).

## Example

**Example:**

- Input:
  Matrix A (M×N):
  Vector x (length N)
- Output:
  Vector y (length M)

*(Specific values are not provided in the original problem statement.)*

## Constraints

- 1 ≤ M, N ≤ 10,000
- The matrix **A** is approximately 60-70% sparse
- Use only CUDA native features (no external libraries)
- The final result must be stored in vector **y**

## Solution

See [sparse_matrix_vector_multiplication.py](./sparse_matrix_vector_multiplication.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Sparse Matrix-Vector Multiplication](https://leetgpu.com/challenges/sparse-matrix-vector-multiplication)
