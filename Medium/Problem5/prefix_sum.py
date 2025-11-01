import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    output[0] = input[0]

    i = 1
    while i < N:
        output[i] = input[i] + output[i - 1]
        i += 1
