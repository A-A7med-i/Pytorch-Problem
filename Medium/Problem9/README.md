# Categorical Cross Entropy Loss (Medium)

This problem requires you to calculate the **categorical cross-entropy loss** for a batch of predictions using CUDA, **without using any external libraries**.

## Problem Statement

Given:

- `logits`: A matrix of predicted logits of size `N × C` (N samples, C classes)
- `true_labels`: A vector of true class labels of size `N`
- `N`: Number of samples
- `C`: Number of classes

Compute the average categorical cross-entropy loss over the batch.
For a single sample with logits and true label, the loss is calculated using the numerically stable formula:

```
loss_i = -log(softmax(logits_i)[true_label_i])
```

where softmax is computed in a numerically stable way.

The final output should be the average loss over all samples, stored in the variable `loss` (a pointer to a single float).

## Example

**Example 1:**

- Input:
  N = 2, C = 3
  logits = [[1.0, 2.0, 0.5], [0.1, 3.0, 1.5]]
  true_labels = [1, 1]
- Output:
  loss = [0.3548926]

**Example 2:**

- Input:
  N = 3, C = 4
  logits = [[-0.5, 1.5, 0.0, 1.0], [2.0, -1.0, 0.5, 0.5], [0.0, 0.0, 0.0, 0.0]]
  true_labels = [3, 0, 1]
- Output:
  loss = [0.98820376]

## Constraints

- 1 ≤ N ≤ 10,000
- 2 ≤ C ≤ 1,000
- -10.0 ≤ logits[i, j] ≤ 10.0
- 0 ≤ true_labels[i] ≤ C
- No external libraries are allowed.
- The final result (average loss) must be stored in the variable `loss`.

## Solution

See [categorical_cross_entropy_loss.py](./categorical_cross_entropy_loss.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Categorical Cross Entropy Loss](https://leetgpu.com/challenges/categorical-cross-entropy-loss)
