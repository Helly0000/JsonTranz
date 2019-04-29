import re
from tqdm import tqdm
import csv
import codecs
from helper import *
import hashlib # didn't used in this py
import json

filenamelist = getfilenamelist()
md5 = hashlib.md5()
for filename in filenamelist:
    with codecs.open(filename+".csv", "r", encoding="utf-8-sig") as csvFile:
        reader = csv.reader(csvFile)
        x = {}
        for item in reader:

            x[item[0]] = item[-1]
            # print(item[-1])

    print('read done')
    newlines = []
    with codecs.open(filename+".txt", "r", encoding="utf-8-sig") as file:
        s = json.load(file)
        for item in s:
            K = item['path'] # the key
            # E = item['pairs'][0]['LocalizedString'] # English
            # C = item['pairs'][-1]['LocalizedString'] # Chinese LocalizedString
            # R = item['pairs'][1]['LocalizedString'] # Russian, which is original words.
            if K in x:
                item['pairs'][-1]['LocalizedString'] = x[K]
    with codecs.open(filename+".txt", "w", encoding="utf-8-sig") as file:
        json.dump(s,file,ensure_ascii=False,indent=2)
