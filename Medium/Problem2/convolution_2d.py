import torch
import torch.nn.functional as F


def solve(
    input: torch.Tensor,
    kernel: torch.Tensor,
    output: torch.Tensor,
    input_rows: int,
    input_cols: int,
    kernel_rows: int,
    kernel_cols: int,
):

    input = input.view(1, 1, input_rows, input_cols)

    bathces = F.unfold(input, (kernel_rows, kernel_cols))

    kernel = kernel.view(-1, 1)

    result = (kernel.T @ bathces).view(-1)

    output.copy_(result)
