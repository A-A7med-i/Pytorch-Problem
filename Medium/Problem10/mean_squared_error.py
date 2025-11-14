import torch


def solve(predictions: torch.Tensor, targets: torch.Tensor, mse: torch.Tensor, N: int):
    diff = predictions[:N] - targets[:N]

    squared = diff * diff

    cost = squared.sum() / N

    mse[0] = cost
