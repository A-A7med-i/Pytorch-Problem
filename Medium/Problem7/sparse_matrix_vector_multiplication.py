import torch


# A, x, y are tensors on the GPU
def solve(A: torch.Tensor, x: torch.Tensor, y: torch.Tensor, M: int, N: int, nnz: int):
    A_matrix = A.view(M, N)

    result = (A_matrix * x).sum(dim=1)

    y.copy_(result)
