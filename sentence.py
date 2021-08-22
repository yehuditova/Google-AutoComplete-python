class Sentence:
    def __init__(self, sentence, location, index):
        self.sentence = sentence
        self.location = location
        self.sentence_index = index

    def get_sentence(self):
        return self.sentence

    def get_location(self):
        return self.location

    def get_sentence_index(self):
        return self.sentence_index
