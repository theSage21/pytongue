import pickle


def ask_token(token):
    "Ask for a token"
    new_token = input(token)
    return {new_token: token}


def ask_mapping(token_list):
    "Asks the user for a mapping"
    mapping = {}
    for token in token_list:
        mapped = ask_token(token)
        mapping.update(mapped)
    translation_name = input('Enter name of mapping: ')
    f = open(translation_name, 'wb')
    pickle.dump(mapping, f)
    f.close()


if __name__ == '__main__':
    import keyword
    ask_mapping(keyword.kwlist + dir(__builtins__))
