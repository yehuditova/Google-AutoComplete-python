from completion import Completion
from initialization import Initialization


class CLI:
    def __init__(self, completion):
        self.completion = completion

    def run(self):
        while True:
            print("Enter your text:")
            text = input()
            sentences = self.completion.search_completions(text)
            if sentences == "not found":
                print("The sentence was not found")
            elif sentences is not None:
                # sentences.sort()
                for i in range(len(sentences)):
                    print(
                        f'{i + 1}. {sentences[i].get_sentence()} ({sentences[i].get_location()},{sentences[i].get_sentence_index()})')


if __name__ == '__main__':
    initialize = Initialization('pages')
    initialize.initialize()

    completion = Completion()
    CLI = CLI(completion)
    CLI.run()
