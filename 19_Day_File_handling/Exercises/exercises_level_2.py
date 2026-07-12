import re
def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        d = f.read().splitlines()
    emails = sorted(list(set([e[6:] for e in d if e[:5] == 'From:'])))
    return emails

from collections import Counter

def most_common_words(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as f:
        d = f.read()
    words = sorted([(v,k) for k,v in dict(Counter(re.findall(r'\b\w+\b', d))).items()], reverse=True)[:n]
    return words

import csv
def hacker(file_path):
    p, js, j = 0, 0, 0
    with open(file_path, 'r', encoding='utf-8') as f:
        d = csv.reader(f, delimiter=',')
        for l in d:
            s = l[1].split()
            if 'python' in s or 'Python' in s:
                p += 1
            if 'javaScript' in s or 'JavaScript' in s or 'javascript' in s:
                js += 1
            if 'java' in s or 'Java' in s:
                j += 1
    return p, js, j

if __name__ == "__main__":
    print("1:", extract_emails('data/email_exchanges_big.txt'))
    print("3.i", most_common_words('data/obama_speech.txt',10))
    print("3.ii", most_common_words('data/michelle_obama_speech.txt',10))
    print("3.iii", most_common_words('data/donald_speech.txt',10))
    print("3.iv", most_common_words('data/melina_trump_speech.txt',10))
    #skip 4
    print("5:", most_common_words('data/romeo_and_juliet.txt', 10))
    print("6:", hacker('data/hacker_news.csv'))
