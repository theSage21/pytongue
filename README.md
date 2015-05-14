PyTongue
========

A program to allow you to write python code in any language.
The basic python language is translated and ready for offline use.
You can add your own languages. Third party-libraries are sadly not supported.

Languages
---------

In order to train a new language use the [Wikipedia list of ISO-codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

Train new languages by:
1. cd languages
2. python3 map_generator.py
3. enter the language code you want to train.

Usage
-----

1. Write source code in your natural language.
2. The first line of the source code must be # lang_code
    1. lang_code must be supported by translate.google.com
    2. lang_code must be specified
3. Run with ./pytongue.sh my_code.py instead of python mycode.py
