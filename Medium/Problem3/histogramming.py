import torch


def solve(input: torch.Tensor, histogram: torch.Tensor, N: int, num_bins: int):
    counts = torch.bincount(input, minlength=num_bins)

    histogram.copy_(counts[:num_bins])
