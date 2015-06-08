PyTongue
========

A program to allow you to write python code in any language.
The basic python language is translated and ready for offline use.
You can add your own languages. Non standard-libraries are sadly not supported.
Yet!!

Languages
---------

In order to train a new language use the [Wikipedia list of ISO-codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

The codes must be supported by [Google Translate](https://translate.google.com)

Train new languages by:

1. `cd languages`
2. `python3 map_generator.py`
3. enter the language code you want to train.

You can generate new examples with the `make_examples.py` file.

Usage
-----

1. Write source code in your natural language.
2. The first line of the source code must be `# lang_code`
3. The `lang_code` must be supported by translate.google.com
4. The `lang_code` must have a mapping present in the languages folder.
5. Run with `./pytongue.sh my_code.py` instead of `python mycode.py`
