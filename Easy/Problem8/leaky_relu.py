import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    alpha = 0.01

    output[:N] = torch.maximum(input[:N], alpha * input[:N])
