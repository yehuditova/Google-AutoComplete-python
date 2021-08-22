from trie import Trie


class SentencesCollection:
    __instance = None
    __init=None

    def __new__(cls, *args, **kwargs):
        if not SentencesCollection.__instance:
            SentencesCollection.__instance = object.__new__(cls)
        return SentencesCollection.__instance

    def __init__(self):
        if not SentencesCollection.__init:
            self.sentences_collection = {}
            self.__sen_counter = 0
            SentencesCollection.__init='initialized'

    def add_sentence_obj(self, sentence_object):
        # print(self.sentences_collection)
        self.__sen_counter += 1
        self.sentences_collection[str(self.__sen_counter)] = sentence_object

        my_tree = Trie.getInstance()
        sentence=sentence_object.get_sentence()

        while sentence.find(' ')>-1:
            my_tree.insert(sentence,self.__sen_counter)
            sentence=sentence[sentence.find(' ')+1:]
        my_tree.insert(sentence, self.__sen_counter)

    def get_sentence_obj(self, id):
        return self.sentences_collection.get(id)

    def get_sentences_collection(self):
        return self.sentences_collection


