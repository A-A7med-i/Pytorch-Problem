import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    sum = input[:N].sum()

    output[0] = sum
