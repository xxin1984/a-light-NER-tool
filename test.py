from GlobalPara import Paras
from Evaluation import MyEvaluation
import torch.optim as optim
from myLSTM import *

torch.manual_seed(2)

Paras.init()

model = MyBiLSTM()

optimizer = optim.SGD(model.parameters(), lr=0.01, weight_decay=1e-4)

with torch.no_grad():
    sentence = torch.tensor(Paras.TRAINING_DATA[0][0], dtype=torch.long)
    print([Paras.IX_TO_TAG[x] for x in Paras.TRAINING_DATA[0][1]])
    tensor_result = model(sentence)
    print([Paras.IX_TO_TAG[x.item()] for x in tensor_result])

for epoch in range(100):
    print(epoch)
    for sentence, tags in Paras.TRAINING_DATA:
        #step 1
        model.zero_grad()
        #step 2 turn in tensors
        sentence_in = torch.tensor(sentence, dtype=torch.long)
        tags_in = torch.tensor(tags, dtype=torch.long)
        #step 3 run forward pass
        loss = model.neg_log_likelihood(sentence_in, tags_in)
        #step 4 compute the gradient
        loss.backward()
        optimizer.step()
    loss_dev, accuracy_dev = MyEvaluation.get_loss(model)
    print(loss_dev)
    print(accuracy_dev)

with torch.no_grad():
    sentence = torch.tensor(Paras.TRAINING_DATA[0][0], dtype=torch.long)
    tensor_result = model(sentence)
    print([Paras.IX_TO_TAG[x.item()] for x in tensor_result])


