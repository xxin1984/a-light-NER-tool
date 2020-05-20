from utilGeneral import *


class Paras:

    HIDDEN_DIM = 10
    EMBEDDING_DIM = 10
    HIDDEN_DIM = 10
    VOC_SIZE = 0
    TAG_SIZE = 0
    WORD_TO_IX = {}
    IX_TO_WORD = {}
    TAG_TO_IX = {}
    IX_TO_TAG = {}
    TRAINING_DATA = []
    DEV_DATA = []

    @staticmethod
    def init():
        lines = my_open_file("nerDataset\\wordList.txt")
        for line in lines:
            Paras.WORD_TO_IX[line.split(" ")[0]] = int(line.split(" ")[1])
            Paras.IX_TO_WORD[int(line.split(" ")[1])] = line.split(" ")[0]

        Paras.VOC_SIZE = len(Paras.WORD_TO_IX)

        lines = my_open_file("nerDataset\\posList.txt")
        for line in lines:
            Paras.TAG_TO_IX[line.split(" ")[0]] = int(line.split(" ")[1])
            Paras.IX_TO_TAG[int(line.split(" ")[1])] = line.split(" ")[0]

        Paras.TAG_SIZE = len(Paras.TAG_TO_IX)

        tmp_list = read_data("nerDataset\\test.txt")

        for terms, tags in tmp_list:
            term_ixs = [Paras.WORD_TO_IX[x] for x in terms]
            tags_ixs = [Paras.TAG_TO_IX[x] for x in tags]
            Paras.TRAINING_DATA.append((term_ixs, tags_ixs))

        tmp_list = read_data("nerDataset\\test.txt")

        for terms, tags in tmp_list:
            term_ixs = [Paras.WORD_TO_IX[x] for x in terms]
            tags_ixs = [Paras.TAG_TO_IX[x] for x in tags]
            Paras.DEV_DATA.append((term_ixs, tags_ixs))


def read_data(path):
    lines = my_open_file(path)
    result = []
    terms = []
    tags = []
    for line in lines:
        if len(line) > 0:
            terms.append(line.split(" ")[0])
            tags.append(line.split(" ")[1])
        else:
            result.append((terms, tags))
            terms = []
            tags = []
    if len(terms) > 0:
        result.append((terms, tags))
    return result
