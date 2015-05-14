#! /bin/bash

python3 translator.py $1
mv temp_translation_file.py trans_$1
python3 trans_$1
