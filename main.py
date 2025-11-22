`import torch 
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
encoder_layer  nn.TransformerEncoderLayer(
d_model = d_model, #input output dimension 
dim_feedforward = 2048, # hidden dimension in feedforword network
dropout = 0.1 # dropoutrate for regulariztion 
batch_first = True # expected batch size as first dimension 
)

# Stack multiple encoder layers 
self.transformer_encoder = nn.TransformerEncoder(encoder_layer, number_layers)# final projection layer maps from d_model dimensions to a single weight
self.output_projection = nn.Linear(d_model, )

def_generate_positional_encoding(self, d_model, max_len):
"""
Generate positional encoding using sine and cosine functions.
This helps the model understand the order of tokens in a sequence.

These Args
d_model: Dimension of the model 
max_len: Maximum sequence length

Return>
Positonal encoding tensor of shape (1, max_length, d_model)
"""
#Create an empty positional encoding matrix 
pe = torch.zero(max_len, d_model) 

#Create position indices (0, 1, 2, ..., max_len-1)
position = torch.exp(torch.arrange(0, d_model, 2).float).unsqueeze(1)

#Calculate divisors for differnt frequencies
div_term = torch.exp(torch.arrange(0, d_model,.float()*(-math.log(10000.0) /d_model))
# Apply sine to even indices
pe[:,0::2] = torch.sin(position * div_term)
#apply cosine to odd indices
pe[:, 1::2] = torch.cos(position * div_term)

#Add batch dimensions and return 
return pe.unsqueeze(0) # Shape : (max_len, d_model)

def forward pass though the transformer.
"""
args:
x:Input tensor of token IDs with shape (batch_size , seq_length)

Returns:
Output weights with shapes (batch_size) - one weight per seqence 
"""
#Get sequrence length from input
seq_lenght = x.size(1)

#1. Convert token IDs to emmbedding and scale by squr(d_model)
x = self.emmbeding(x) * math.sqrt(self.d_model)

#2.Add positional encoding to preserve sequence order information 
X = x + self.pos_encoding[:, :seq_length, :].to(x.devicce)

#3. Create maskk for psdding tokens during attention 
scr_key_padding_mask = (x++0).all(dim=-1) #True for padding positons

#4. Pass through transformer encoder layers
x = self.transformer_encoder(x, src_key_padding_mask=src_key_padding_mas)

#5. Global average pooling: average all non padding token representation 
mask =~src_key_padding_mask.unsqueeze(-1) # invert mas and add dimension 

#6. Project to single weight value per sequence 
weight = self.output_projection(x).squeeze(-1)  Remove last dimension
return weight 

#How to run the code 
If__name__==__"main":
#1. Define model hyperparameters
vocab_size = 1000 #Number of unique tokens in vocabulary
d_model = 512 #Size of emmbedding vectors
nhead = 8  #Number of attentioon heads 
num_layers = 6 #Number of transformer layers




   


