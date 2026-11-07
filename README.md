# Self-Supervised Depth Estimation at Scale

Official implementation of the paper **Self-Supervised Depth Estimation at Scale** (CVPR 2025).

This repository contains the complete, released implementation used for all
experiments reported in the paper, including data preparation, model code and
evaluation scripts.

## Repository layout

- `src/` - depth network, losses and training loop
- `data/` - video frame sampling and augmentation
- `experiments/` - Eigen and KITTI evaluation scripts

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Training

```bash
bash experiments/run_all.sh
```

## Citation

```bibtex
@inproceedings{rivera2025depth,
  title={Self-Supervised Depth Estimation at Scale},
  author={Rivera, Janet and Lindqvist, Tomas},
  booktitle={CVPR},
  year={2025}
}
```
