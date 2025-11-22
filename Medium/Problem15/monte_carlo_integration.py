import torch


def solve(
    y_samples: torch.Tensor, result: torch.Tensor, a: float, b: float, n_samples: int
):
    avg = torch.mean(y_samples)

    result_value = (b - a) * avg

    result.copy_(result_value)
