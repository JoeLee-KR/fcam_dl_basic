# bellow for python3.7,
# not need over python3.8
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import numpy as np
print('>numpy np:',np.__version__)

import scipy as sp
print('>scipy sp:',sp.__version__)

import torch as tp
tp.__version__
print(">pyTorch tp:", tp.__version__)

import tensorflow as tf
print(">Tensorflow:", tf.__version__)

print("Test End. by PY")