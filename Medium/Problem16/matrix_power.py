import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, P: int):
    A = input.view(N, N)

    result = torch.matrix_power(A, P)

    output.copy_(result)
