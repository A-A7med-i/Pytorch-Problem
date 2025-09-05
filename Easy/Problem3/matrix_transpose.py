import torch


def solve(input: torch.Tensor, output: torch.Tensor, rows: int, cols: int):
    transpose_input = input.t()

    output.copy_(transpose_input)
