import os
import pickle


def tokenify(string):
    tokens = string.split(' ')
    while '' in tokens:
        tokens.remove('')
    return tokens


class Translator:
    """
    Open file.
        for every line.
            get tokens
            translate
            generate tokens
            write to output
    """
    def __init__(self, input_file_path):
        self.__open_files(input_file_path)

    def __close_files(self):
        self.inp.close()
        self.out.close()

    def __open_files(self, input_file_path):
        self.input_file_path = os.path.abspath(input_file_path)
        self.output_file_path = os.path.abspath('temp_translation_file.py')
        self.inp = open(self.input_file_path, 'r')
        self.out = open(self.output_file_path, 'w')
        self.language = self.inp.readline()[2:]
        f = open(os.path.join(os.path.split(os.getcwd())[0], 'langauges', self.language), 'rb')
        self.mapping = pickle.load(f)
        f.close()

    def __lookup(self, tokens):
        "Lookup in mapping"
        new_tokens = []
        while len(tokens) != 0:
            left, right = tokens[0], tokens[1:]
            translation = self.mapping[left]
            new_tokens.append(translation)
            tokens = right
        return new_tokens

    def translate(self, filepath=None):
        if filepath is not None:
            self.__open_files(filepath)
        # begin translation
        for line in self.inp.readlines():
            line = line.strip()
            tokens = tokenify(line)
            new_tokens = self.__lookup(tokens)
            new_line = ' '.join(new_tokens)
            self.out.write(new_line + '\n')
        self.__close_files()
