import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    zero = torch.tensor(0.0, device=input.device)

    output[:N] = torch.max(input[:N], zero.expand_as(input[:N]))
