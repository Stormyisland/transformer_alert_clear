import torch 
import torch.nn as nn
import math 
class SimpleTransformer(nn.Module):
  def __init__(self, vocab_size, d_model = 512, nhead=8, Layers = 6, maxseq_length = 512):
"""
Initialize the simple Transformer model.

args: 
vocab_size : size of the vocabulary (number of unique tokens)
d_model: Dimension of emmbeding vectors (default 5122)
nhead : Number of attention headds (default 8)
num_layers : Number of transformer encoder layers (default 6)
max_seq_lengt: Maximum sequence length the model can handle (default 512)
"""
super(SimpleTransformer, self).__init__()
self.d_model

#embedding layer: converts token IDs to dense vectors
self.emmbedding + nn.Embedding(vocab_size, d_model)
#Generate positional encodings (fixed sine?cosign patterns)
self.pos_encode = self.generate_positional_encoding(d_model, max_seq_lenth)
#Create transformer encoder layers
encoder_lyer  nn.TransformerEncoderLayer(
  d_model = d_model, #input output dimention 
    dim_feedforward = 2048, # hidden dimension in feedforword network
  dropout = 0.1 # dropoutrate for regulariztion 
  batch_first = True # expected batch size as first dimension 
  )

# Stack multiple encoder layers 
srelf.transformer_encoder = nn.TrransformerEncoder(encoder_layer, number_layers)

