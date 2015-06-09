import os
import json


def tokenify(string):
    for i in "[]{}()-=+/<>.,''" + '"':
        string = string.replace(i, ' ' + i + ' ')
    tokens = string.split(' ')
    while '' in tokens:
        tokens.remove('')
    for t in tokens:
        t = t.strip()
    return tokens


def get_indent(line):
    count = 0
    for i in line:
        if i == ' ':
            count += 1
        else:
            break
    return count


def reconstruct_line(tokens, indent):
    string = ' '.join(tokens)
    for i in "[]{}()-=+/<>.,''" + '"':
        string = string.replace(' ' + i + ' ', i)
        string = string.replace(' ' + i, i)
        string = string.replace(i + ' ', i)
    string = string.strip()
    string = (' ' * indent) + string
    return string


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
        first_line = self.inp.readline()
        if first_line[0] != '#':
            raise Exception("Language not found")
        self.language = first_line[2:].strip().upper()
        f = open(os.path.join(os.getcwd(), 'languages', self.language), 'r')
        self.mapping = json.loads(''.join(f.readlines()))
        f.close()

    def __lookup(self, tokens):
        "Lookup in mapping"
        new_tokens = []
        for token in tokens:
            try:
                # print('trying: ', token)
                translation = self.mapping[token]
            except KeyError:
                # print('Exception')
                translation = token
            new_tokens.append(translation)
        return new_tokens

    def translate(self, filepath=None):
        if filepath is not None:
            self.__open_files(filepath)
        # begin translation
        for line in self.inp.readlines():
            indent = get_indent(line)
            line = line.strip()
            tokens = tokenify(line)
            new_tokens = self.__lookup(tokens)
            new_line = reconstruct_line(new_tokens, indent)
            # print(new_line)
            self.out.write(new_line + '\n')
        self.__close_files()

if __name__ == '__main__':
    import sys
    tr = Translator(sys.argv[1])
    tr.translate()
