import numpy as np
from white_tensor_fabric.engine.runtime import CognitionLoop

# Initialize the cognitive fabric engine
# 4 latent branches, 3-dimensional coordinate base, local energy cap = 3.5
engine = CognitionLoop(num_branches=4, dim=3, cap=3.5)

# Generate an incoming stimulus matching a dormant background wave profile
stimulus = np.array([0.8, -0.2, 0.5])
phase = 0.42

# Execute one complete runtime cycle:
# Wave Resonance -> Phase Interference -> Metric Dilation -> Tensor Contraction
contraction_output, committed_branch = engine.step(stimulus, phase)

print(f"Contracted Output Tensor Shape: {contraction_output.shape}")
print(f"Phase-Coherent State Commit: Branch #{committed_branch}")
