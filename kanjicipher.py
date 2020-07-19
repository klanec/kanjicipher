#!/usr/bin/env python

import xml.etree.ElementTree as ET
import random
from tqdm import tqdm
import sys


try:
    print("Loading KANJIDIC2...", end="")
    TREE = ET.parse('kanjidic2.xml')
    print("done.")
except FileNotFoundError:
    print("No kanjidic2.xml found in this directory. Make sure to download and extract!\n")
    print("http://www.edrdg.org/kanjidic/kanjidic2.xml.gz\n")
    sys.exit()


ROOT = TREE.getroot()


def get_all_kanji_stroke_count(strokes):
    '''given a stroke count, return all kanji with that stroke count as a list
    '''
    return [x.findtext('literal') for x in ROOT if x.findtext('misc/stroke_count') == str(strokes)]


def get_dict_kanji_stroke():
    '''Loads all kanji in kanjidic2 into a python dictionary of {KANJI:STROKE_CNT}
    '''
    return {x.findtext('literal'):x.findtext('misc/stroke_count') for x in ROOT}


def encrypt(plain):
    ''' If the character is encodable (ie, its value can be translated to the MAX strokes)
    then take the ASCII value minus 96 and randomly select a kanji with that stroke count
    '''
    strokes = {x.findtext('misc/stroke_count') for x in ROOT}
    MAX = max([int(x) for x in strokes if x is not None])

    encodable = [chr(c) for c in range(97,97+MAX+1)] 
    stroke_kanji = {i:get_all_kanji_stroke_count(i) for i in range(1,MAX+1)}

    cipher = [random.choice(stroke_kanji[ord(c.lower()) - 96]) if c.lower() in encodable else c.lower() for c in tqdm(plain)]

    return "".join(cipher)
        

def decrypt(cipher):
    '''Load in a dictionary of all kanji and their corresponding stroke counts to a dictionary 
    '''
    stroke_counts = get_dict_kanji_stroke()   

    plain = [chr(96 + int(stroke_counts[c])) if c in stroke_counts.keys() else c for c in tqdm(cipher)] 

    return "".join(plain)


def main():

    if len(sys.argv) < 3:
        print("\nUsage: kanjicipher.py [-d | -e] FILE\n")
        sys.exit()

    file = sys.argv[-1]
    op = sys.argv[-2]
    stem = file.split(".")[0]

    operation = {"-e":encrypt, "-d":decrypt}

    with open(file, "r") as rp, open(stem+"_"+operation[op].__name__+".txt", "w") as wp:
        print(operation[op].__name__)
        in_text = rp.read()
        out_text = operation[op](in_text)
        wp.write(out_text)


if __name__=="__main__":
    main()