# PyTongue

This little piece of code lets you write python code in any language you deem fit.
This is meant as a tool to teach people programming without having to teach them English first.

Python3.x is supported.

The basic python language is translated and ready for offline use.
You can add your own languages. Non standard libraries are not yet supported.

Working
-------

This is a simple transliteration program. The idea is as follows.

1. Get a mapping for a language from Google translate.
2. Store the mapping as a dictionary.
3. Get a sample source file.
4. Identify what language it is written in.
5. Load the required language and translate into normal Python.
6. Run the newly generated file.

Installing
----------

```
git clone https://github.com/theSage21/pytongue.git
cd pytongue
git submodule init
git submodule update
```

Languages
---------

In order to train a new language use the [Wikipedia list of ISO-codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

The codes must be supported by [Google Translate](https://translate.google.com)

Get new languages by:

1. `cd languages`
2. `python3 map_generator.py`
3. enter the language code you want to train.

Usage
-----

1. Write source code in your natural language.
2. The first line of the source code must be `# lang_code`
    1. The `lang_code` must be supported by translate.google.com
    2. The `lang_code` must be specified in the source file
3. Run with `./pytongue.sh my_code.py` instead of `python mycode.py`

Example
-------

If you were to write a useless example in Hindi it might be something like this.

```
# HI
छाप('नमस्ते दुनिया!')
के_लिए i में range(10):
    छाप(i)
जबकि 1:
    छाप('नमस्ते दुनिया!')
```

This translates to

```
# HI
print('Hello world!')
for i in range(10):
    print(i)
while 1:
    print('Hello World!')
```

To generate examples in other languages:

1. Create a mapping for the required language. (we assume ES here)
2. Go to root folder and `python3 make_examples.py`
3. You example is generated in `examples/ES_example.py`

To generate a different example edit the `examples/example.py` file.

What if languages do not translate properly?
--------------------------------------------

If the translation provided by Google feels wrong there is nothing to worry about.
Since the translation is actually implemented using a dictionary, all you have to do is change the key-value pairs.

What is the Google part again?
------------------------------

That is to automate the process of translation mapping. Translating a lot of words gets tiring very quickly.

You can create your own mapping if you want in any language you want.
