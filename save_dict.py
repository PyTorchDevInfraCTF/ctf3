import torch

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.x = torch.Tensor([0, 0, os.environ["SECRET"]]) # Change the numbers to what you need
        self.numbers = torch.nn.Parameter(self.x)

    def forward(self):
        return torch.sum(self.numbers)


model = Model()
torch.save(model.state_dict(), "weights.pt")
