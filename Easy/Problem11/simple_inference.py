import torch
import torch.nn as nn


def solve(input: torch.Tensor, model: nn.Module, output: torch.Tensor):
    with torch.inference_mode():
        result = model(input)
        output.copy_(result)
