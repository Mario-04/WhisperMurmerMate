import os
import numpy as np

try:
    import tensorflow  # required in Colab to avoid protobuf compatibility issues
    print("TensorFlow version:", tensorflow.__version__)
except ImportError:
    print("TensorFlow version not found")
    pass

import torch
import pandas as pd
import whisper
import torchaudio

from tqdm.notebook import tqdm


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(DEVICE)