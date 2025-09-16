import torch


def solve(A: torch.Tensor, B: torch.Tensor, N: int):
    B[:N, :N] = A[:N, :N]
