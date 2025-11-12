import torch
import torch.nn.functional as F


def solve(
    logits: torch.Tensor, true_labels: torch.Tensor, loss: torch.Tensor, N: int, C: int
):
    log_probs = F.log_softmax(logits, dim=1)

    true_log_probs = log_probs[torch.arange(N, device=logits.device), true_labels]

    loss[0] = -true_log_probs.mean()
