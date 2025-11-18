import torch


def solve(
    A: torch.Tensor,
    B: torch.Tensor,
    C: torch.Tensor,
    BATCH: int,
    M: int,
    N: int,
    K: int,
):
    A32 = A.to(torch.float32).reshape(BATCH, M, K)
    B32 = B.to(torch.float32).reshape(BATCH, K, N)

    result = torch.bmm(A32, B32)

    C.copy_(result.to(C.dtype))
