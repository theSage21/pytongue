import pickle
from translate import Translator


def ask_mapping(token_list):
    "Asks the user for a mapping"
    translation_name = input('Enter code of target language("in" for hindi): ')
    translation_name = translation_name.upper().strip()
    translator = Translator(to_lang=translation_name)
    mapping = {}
    for token in token_list:
        translation = translator.translate(token)
        translation = translation.replace(' ', '_').strip()
        mapped = {translation: token}
        print(mapped)
        mapping.update(mapped)
    f = open(translation_name, 'wb')
    pickle.dump(mapping, f)
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
    ask_mapping(keys + needed)
