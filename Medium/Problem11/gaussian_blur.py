import torch
import torch.nn.functional as F


# input, kernel, output are tensors on the GPU
def solve(
    input: torch.Tensor,
    kernel: torch.Tensor,
    output: torch.Tensor,
    input_rows: int,
    input_cols: int,
    kernel_rows: int,
    kernel_cols: int,
):

    img = input.view(1, 1, input_rows, input_cols)

    ker = kernel.view(1, 1, kernel_rows, kernel_cols)

    pad_h = kernel_rows // 2
    pad_w = kernel_cols // 2

    blurred = F.conv2d(img, ker, padding=(pad_h, pad_w))

    output.copy_(blurred.view(input_rows, input_cols))
