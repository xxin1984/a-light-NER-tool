import torch
from GlobalPara import *

class MyEvaluation:

    def __init__(self):
        pass

    @staticmethod
    def get_loss(model):
        loss = 0.0
        true_num = 0.0
        false_num = 0.0

        for sentence, tags in Paras.DEV_DATA:
            with torch.no_grad():
                sentence_in = torch.tensor(sentence, dtype=torch.long)
                tags_in = torch.tensor(tags, dtype=torch.long)
                tags_pred = model(sentence_in)
                for i, tag in enumerate(tags):
                    if tags[i] == tags_pred[i].item():
                        true_num = true_num+1
                    else:
                        false_num = false_num+1
                loss_sentence = model.neg_log_likelihood(sentence_in, tags_in)
                loss = loss+loss_sentence.item()
        accuracy = true_num / (true_num+false_num)
        return loss, accuracy





