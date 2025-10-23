import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, K: int):
    count = (input[:N] == K).sum()

    output[0] = count
