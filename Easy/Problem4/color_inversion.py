import torch


def solve(image: torch.Tensor, width: int, height: int):
    pixels = image.view(-1, 4)

    pixels[:, :3] = 255 - pixels[:, :3]
