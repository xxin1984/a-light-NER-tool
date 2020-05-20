import torch
import torch.nn as nn
from GlobalPara import Paras


class MyBiLSTM(nn.Module):

    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(Paras.EMBEDDING_DIM, Paras.HIDDEN_DIM,
                            num_layers=1, bidirectional=True)
        self.word_embeddings = nn.Embedding(Paras.VOC_SIZE, Paras.EMBEDDING_DIM)
        self.hidden_to_tag = nn.Linear(Paras.HIDDEN_DIM*2, Paras.TAG_SIZE)


    def forward(self, sentence):
        lstm_feat = self._get_lstm_features(sentence)
        values, idx = torch.max(lstm_feat, 1)
        return idx


    def neg_log_likelihood(self, sentence, tags):
        lstm_feat = self._get_lstm_features(sentence)
        result = torch.tensor(0.0)
        for i, feat in enumerate(lstm_feat):
            ix = tags[i]
            tmp = torch.logsumexp(feat[ix], 0)-torch.logsumexp(feat, 0)
            result = result-tmp

        return result


    def _get_lstm_features(self, sentence):
        embeds = self.word_embeddings(sentence)
        lstm_input = embeds.view(sentence.size()[0], 1, Paras.EMBEDDING_DIM)
        lstm_out, last_state = self.lstm(lstm_input, (torch.randn(2, 1, Paras.HIDDEN_DIM),
                                                      torch.randn(2, 1, Paras.HIDDEN_DIM)))
        feat_input = lstm_out.view(sentence.size()[0], Paras.HIDDEN_DIM * 2)
        lstm_feat = self.hidden_to_tag(feat_input)
        return lstm_feat





