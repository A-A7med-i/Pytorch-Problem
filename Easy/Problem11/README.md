# Simple Inference (Easy)

This problem requires you to run inference on a PyTorch model. Given an input tensor and a trained `torch.nn.Linear` model, compute the forward pass and store the result in the output tensor.

## Problem Statement

Given:

- An input tensor of shape `(batch_size, input_size)`
- A loaded `torch.nn.Linear` model with:
  - `weight` of shape `[output_size, input_size]`
  - `bias` of shape `[output_size]`

Compute the output using the linear transformation:

```python
output = input @ weight.T + bias
```

Store the result in the provided output tensor.

## Example

**Example 1:**

- Input:
  `input = [[1.0, 2.0]]`  (batch_size=1, input_size=2)
  model: Linear layer with `weight=[[0.5, 1.0], [1.5, 0.5]]`, `bias=[0.1, 0.2]`
- Output:
  `output = [[2.6, 2.7]]`  (batch_size=1, output_size=2)

**Example 2:**

- Input:
  `input = [[1.0], [2.0], [3.0]]`  (batch_size=3, input_size=1)
  model: Linear layer with `weight=[[2.0]]`, `bias=[1.0]`
- Output:
  `output = [[3.0], [5.0], [7.0]]`  (batch_size=3, output_size=1)

## Constraints

- 1 ≤ batch_size ≤ 1,000
- 1 ≤ input_size ≤ 1,000
- 1 ≤ output_size ≤ 1,000
- -10.0 ≤ input values ≤ 10.0
- Use PyTorch's built-in functions and operations
- The model is already loaded and ready for inference
- The final result must be stored in the output tensor

## Solution

See [simple_inference.py](./simple_inference.py) for a PyTorch implementation.

## Additional Information

For more details and to try the problem online, visit:
[Simple Inference](https://leetgpu.com/challenges/simple-inference)
