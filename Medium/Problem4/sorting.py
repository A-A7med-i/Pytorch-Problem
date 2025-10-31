import torch


def solve(data: torch.Tensor, N: int):
    sorted_data, _ = torch.sort(data)

    data.copy_(sorted_data)
