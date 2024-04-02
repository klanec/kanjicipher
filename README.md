# kanjicipher
A a1z26 substitution cipher that converts ASCII text to Japanese Kanji based on kanji-stroke count

This cipher was thought up for RGBctf 2020, in which cipher text produced from it was featured in the cryptography category under the challenge "Grab your jisho"

hello,world! -> 㟁以陽𣷹鋌,鰹嫵擽棽匹!

# Requirements
Used `tqdm` for progress bar, you can simply remove that from the script if you don't want to install it. Otherwise:

`pip3 install tqdm`

# Usage
`python3 kanjicipher.py -e PLAINTEXT.txt`

`python3 kanjicipher.py -d CIPHERTEXT.txt`


# TODO

- make it better
