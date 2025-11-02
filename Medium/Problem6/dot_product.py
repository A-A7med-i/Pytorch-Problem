import torch


def solve(A: torch.Tensor, B: torch.Tensor, result: torch.Tensor, N: int):
    output = torch.dot(A, B)

    # output = torch.tensor(0.0, device=result.device)

    # for i in range(N):
    #     output += A[i] * B[i]

    result[0] = output
