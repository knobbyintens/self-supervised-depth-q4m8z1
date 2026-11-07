import torch


def photometric_loss(warped, target, mask):
    diff = (warped - target).abs().mean(1, keepdim=True)
    return (diff * mask).sum() / mask.sum().clamp_min(1.0)


def smoothness_loss(depth):
    grad = depth[:, :, 1:, :] - depth[:, :, :-1, :]
    return grad.abs().mean()
