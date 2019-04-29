import re
from tqdm import tqdm
import csv
import codecs
from helper import *
import hashlib
import json
from googletrans import Translator
translator = Translator()
translator = Translator(service_urls=[
      'translate.google.com.tw',
    ])

filenamelist = getfilenamelist()

md5 = hashlib.md5()

for filename in filenamelist:
    newlines = []
    with codecs.open(filename+".txt", "r", encoding="utf-8-sig") as file:
        s = json.load(file)
        for item in s:
            K = item['path']
            E = item['pairs'][0]['LocalizedString']
            C = item['pairs'][-1]['LocalizedString']
            R = item['pairs'][1]['LocalizedString']
            if E == '':
                if C == '':
                    try:
                        txt = translator.translate(R, src='ru', dest='zh-CN')
                        newlines.append([K,R,txt.text])
                        print (R,txt.text)
                    except:
                        pass
                else:
                    newlines.append([K,R,C])
            else:
                newlines.append([K,E,C])

    with codecs.open(filename+".csv", "w", encoding="utf-8-sig") as file:
        f_csv = csv.writer(file)
        #f_csv.writerow(['MD5','原文', '翻译'])
        i = 0
        for newline in newlines:
            i = i + 1
            f_csv.writerow(newline)
