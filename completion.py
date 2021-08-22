from trie import Trie
from sentences_collection import SentencesCollection


class Completion:
    def __init__(self):
        self.trie = Trie.getInstance()
        self.sentences_collection = SentencesCollection()
        self.prev_sentences = None
        self.prev_text = None

    def search_completions(self, text):
        if text == '#':
            self.prev_sentences = None
            return
        sentences_id = self.trie.search(text)
        if self.prev_sentences is None:
            sentences = self.get_five_sentences(sentences_id, text)
        else:
            sentences_id = self.get_relevant_sentences(sentences_id)
            sentences = self.get_five_sentences(sentences_id, text)
        if sentences != "not found":
            self.prev_sentences = sentences_id
            self.prev_text = text
        return sentences

    # Extract five objects of sentences by id from the fit sentences id list.
    def get_five_sentences(self, sentences_id, text):
        if len(sentences_id) == 0:
            self.prev_sentences = None
            return "not found"
        completed_sentences = []
        res = []
        i = 0
        while len(completed_sentences) < 5:
            if i == len(sentences_id):
                break
            sen_obj = self.sentences_collection.get_sentence_obj(str(sentences_id[i]))
            sen = sen_obj.get_sentence()
            if self.prev_sentences is None or f'{self.prev_text} {text}' in sen:
                if sen not in res:
                    completed_sentences.append(sen_obj)
                    res.append(sen)
            i += 1
        if len(completed_sentences)==0:
            self.prev_sentences=None
            return "not found"
        return completed_sentences

    # Find the intersection of the previous fit sentences and the current.
    def get_relevant_sentences(self, sentences_id):
        sentences_id = set(sentences_id)
        prev_sen = set(self.prev_sentences)
        sen_ids = []
        if len(sentences_id) < len(prev_sen):
            for id, val in enumerate(sentences_id):
                if val in prev_sen:
                    sen_ids.append(val)
        else:
            for id, val in enumerate(prev_sen):
                if val in sentences_id:
                    sen_ids.append(val)
        return sen_ids
