import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, M: int, K: int):
    count = (input[:N, :M] == K).sum()

    output[0] = count
