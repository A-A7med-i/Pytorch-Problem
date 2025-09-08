import torch


def solve(input: torch.Tensor, N: int):
    input.copy_(input.flip(0))

    # left, right = 0, N - 1

    # while right > left:
    #     temp = input[left]
    #     input[left] = input[right]
    #     input[right] = temp
    #     left += 1
    #     right -= 1
