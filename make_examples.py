#! /bin/bash
import translator as tr
import pickle
import os

here = os.getcwd()

def get_example():
    ex = os.path.join(here, 'examples', 'example.py')
    f = open(ex, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_lines(name):
    f = open(name, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_mapping(filename):
    f = open(filename, 'rb')
    data = pickle.load(f)
    f.close()
    new_data = {}
    for i in data.keys():
        v = data[i]
        new_data[v] = i
    return new_data

def write_example(ln, lines):
    f = open(os.path.join(here, 'examples', ln + '_example.py'), 'w')
    f.writelines([i + '\n' for i in lines])
    f.close()

if __name__ == '__main__':
    example_lines = get_example()
    path = os.path.join(here, 'languages')
    lang = [os.path.join(here, 'languages', i) for i in os.listdir(path) if len(i) == 2]
    for ln in lang:
        print(ln)
        mapping = get_mapping(ln)
        new_lines = ['# ' + os.path.split(ln)[-1]]
        for line in example_lines:
            indent = tr.get_indent(line)
            line = line.strip()
            tokens = tr.tokenify(line)
            new_tokens = []
            for token in tokens:
                try:
                    translation = mapping[token]
                except KeyError:
                    translation = token
                new_tokens.append(translation)
            new_line = tr.reconstruct_line(new_tokens, indent)
            new_lines.append(new_line)
        write_example(os.path.split(ln)[-1], new_lines)
