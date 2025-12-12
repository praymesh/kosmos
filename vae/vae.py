#encoder of VAE with GQ layer
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from torch.nn.utils import weight_norm
#from vector_quantize_pytorch import VectorQuantize  



class Encoder(nn.Module):
    def __init__(self,  input_dim, latent_dim):
        super().__init__()
        # ENCODER: Compresses 64x64 image -> 8x8 latent vector
        
        self.enc = nn.Sequential(
            nn.Conv2d(3,32, kernel_size =4, stride=2, padding =1) ,#input: 64x64x3 -> output: 32x32x32
            nn.LeakyReLU(),
            nn.Conv2d(32,64, kernel_size =4, stride=2, padding =1) ,#input: 32x32x32 -> output: 16x16x64
            nn.LeakyReLU(),
            nn.Conv2d(64,128, kernel_size =4, stride=2, padding =1) ,#input: 16x16x64 -> output: 8x8x128
            nn.LeakyReLU(),
            nn.Conv2d(128,latent_dim, kernel_size =4, stride=2, padding =1) ,#input: 8x8x128 -> output: 4x4xlatent_dim
            nn.Tanh(),  
        )
        def forward(self, x):
            z = self.enc(x) 
            return z
        
class Decoder(nn.Module):
    def __init__(self,latent_dim):
        super().init__()
        # DECODER: Decompresses 8x8 latent vector -> 64x64 image
        self.dec = nn.Sequential(
            nn.Conv2d(latent_dim,128,4,2,1),
            nn.LeakyReLU(),
            nn.Conv2d(128,64,4,2,1),
            nn.LeakyReLU(),
            nn.Conv2d(64,32,4,2,1),
            nn.LeakyReLU(),
            nn.Conv2d(32,3,4,2,1),
            nn.Sigmoid(),  # To ensure output pixel values are between 0 and 1
        )
        def forward(self,x):
            z= self.dec(x)
            return z

class GQ(nn.Module):
    def __init__(self, latent_dim):
        super().__init__()
        
        self.gq = nn.Sequential()
        
    def forward(self,x):
        z = self.gq(x)
        return z


class GQ_VAE(nn.Module):
    def __init__(self,x):
        super().__init__()
        
        
        
        
    def forward(self, x) :  
        enc_op = enc(x)
        gq_op = gq(enc_op)
        dec_op = dec(gq_op)
        
        

def Losses(self, x, output ) :
        recon_loss = F.mse_loss(output, x)
        lpips_loss = self.lpips_loss_fn(output, x).mean()
        kl_loss = self.kl_loss_fn(output, x).mean()
        return recon_loss
        
        
        