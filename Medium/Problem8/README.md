# General Matrix Multiplication (GEMM) (Medium)

This problem requires you to implement a basic General Matrix Multiplication (GEMM) on the GPU, **using only native features (no external libraries except WMMA)**.

## Problem Statement

Given:

- Matrix **A** of dimensions `M × K` (FP16, row-major)
- Matrix **B** of dimensions `K × N` (FP16, row-major)
- Matrix **C** of dimensions `M × N` (FP16, row-major, used as both input and output)
- Scalars `alpha` and `beta` (both FP32)

Compute the operation:

```
C = alpha * (A @ B) + beta * C
```

- Accumulation during multiplication should use FP32 for better precision before converting the final result to FP16.
- The final result must be stored back into matrix **C** as FP16.

## Example

*Note: Specific example values are not provided in the original problem statement. All input matrices are FP16.*

## Constraints

- 16 ≤ M, N, K ≤ 4096
- All matrices are stored in row-major order.
- Use only native features (external libraries other than WMMA are not permitted).
- The solve function signature must remain unchanged.
- The final result must be stored back into matrix **C** as half (FP16).

## Solution

See [GEMM.py](./GEMM.py)for a Python implementation

## Additional Information

For more details and to try the problem online, visit:
[General Matrix Multiplication (GEMM)](https://leetgpu.com/challenges/general-matrix-multiplication-gemm)
