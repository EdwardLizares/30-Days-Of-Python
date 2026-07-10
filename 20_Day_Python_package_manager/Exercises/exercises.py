import requests 

def read_url_romeo_and_juliet():
    response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
    return response.text

def cats_api():
    response = requests.get('https://api.thecatapi.com/v1/breeds')
    d = response.json()
    return d

def r2i(r):
    low, high = map(float, r.split(" - "))
    return (low + high) / 2

from statistics import median, mean, stdev
def cat_weight_stats(d):
    w = [r2i(c['weight']['metric']) for c in d if 'weight' in c]
    return min(w), max(w), mean(w), median(w), stdev(w)

def cat_life_stats(d):
    l = [r2i(c['life_span']) for c in d if 'life_span' in c]
    return min(l), max(l), mean(l), median(l), stdev(l)

from collections import Counter
def cat_country_breed_freq(d):
    return Counter(c["origin"] for c in d), Counter(c["name"] for c in d)

if __name__ == "__main__":
    #print(read_url_romeo_and_juliet()) # soft skip
    d = cats_api()
    print("2.i:", cat_weight_stats(d))
    print("2.ii:", cat_life_stats(d))
    print("2.iii:", cat_country_breed_freq(d))
    #skip3-4 links dont work
