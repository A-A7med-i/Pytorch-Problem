import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, k: int):
    top_values, _ = torch.topk(input[:N], k, largest=True, sorted=True)

    output.copy_(top_values)
