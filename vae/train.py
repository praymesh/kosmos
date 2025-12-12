import torch.nn as nn
import torch.nn.functional as F
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent)) #root dir

from vae.vae import Encoder, Decoder, GQ , GQ_VAE
from configs import latent_dim, device

class VAE_Trainer():
    def __init__(self):
        
        if torch.device(device).type == 'cuda':
            print("Using GPU for training")
        else :
            print("Using CPU for training")
              