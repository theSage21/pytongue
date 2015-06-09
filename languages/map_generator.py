import json
from translate import Translator


def ask_mapping(token_list):
    "Asks the user for a mapping"
    translation_name = input('Enter code of target language("hi" for hindi): ')
    translation_name = translation_name.upper().strip()
    translator = Translator(to_lang=translation_name)
    mapping = {}
    for token in token_list:
        internal = False
        if token[:2] + token[-2:] == '____':
            token = token[2:-2]
            internal = True
        translation = translator.translate(token)
        translation = translation.replace(' ', '_').strip()
        if internal:
            token = '__' + token + '__'
            translation = '__' + translation + '__'
        mapped = {translation: token}
        print(mapped)
        mapping.update(mapped)
    f = open(translation_name, 'w')
    f.write(json.dumps(mapping,
                       ensure_ascii=False,
                       indent=4))
    f.close()


if __name__ == '__main__':
    import keyword
    keys = keyword.kwlist
    builtins = dir(__builtins__)
    needed = []
    for i in builtins:
        if 'Error' in i:
            continue
        if 'Warning' in i:
            continue
        needed.append(i)
    ask_mapping(list(set(keys + needed)))
