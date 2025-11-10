import torch


# A, B, C are tensors on the GPU
def solve(
    A: torch.Tensor,
    B: torch.Tensor,
    C: torch.Tensor,
    M: int,
    N: int,
    K: int,
    alpha: float,
    beta: float,
):
    A32 = A.to(torch.float32).reshape(M, K)
    B32 = B.to(torch.float32).reshape(K, N)
    C32 = C.to(torch.float32).reshape(M, N)

    result32 = alpha * (A32 @ B32) + beta * C32

    C.copy_(result32.to(torch.float16))
