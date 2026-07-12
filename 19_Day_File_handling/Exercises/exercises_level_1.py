def count_lines_and_words(file_path):
    line_count = 0
    word_count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        line_count = len(lines)
        for line in lines:
            word_count += len(line.split())
    return line_count, word_count

import json
def most_spoken_languages(file_path, n):
    with open(file_path, "r", encoding='utf-8') as f:
        s = f.read()
    d = json.loads(s)
    count = {}
    for c in d:
        if 'languages' in c:
            for l in c['languages']:
                if l not in count:
                    count[l]=0
                count[l] += 1
    return sorted([(v, k) for k, v in count.items()], reverse=True)[:n]

def most_populated_countries(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as f:
        s = f.read()
    d = json.loads(s)
    return [dict(country=t[1], population=t[0]) for t in sorted([(c['population'], c['name']) 
                                                for c in d if 'population' in c], reverse=True)[:n]]

if __name__ == "__main__":
    print("1.i:", count_lines_and_words('data/obama_speech.txt'))
    print("1.ii:", count_lines_and_words('data/michelle_obama_speech.txt'))
    print("1.iii:", count_lines_and_words('data/donald_speech.txt'))
    print("1.iv:", count_lines_and_words('data/melina_trump_speech.txt'))
    print("2:", most_spoken_languages('data/countries_data.json', 10))
    print("3:", most_populated_countries('data/countries_data.json', 10))