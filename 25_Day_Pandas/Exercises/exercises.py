import pandas as pd
import csv

def open_hacker():
    with open('data/hacker_news.csv', 'r', encoding='utf-8') as f:
        d = [l for l in csv.reader(f, delimiter=',')]
    return pd.DataFrame(d[1:], columns=d[0])

if __name__ == "__main__":
    data = open_hacker()
    print("2:", data[:5])
    print("3:", data[-5:])
    print("4:", data["title"])
    print("5:", data.shape)
    print("5.1:", data["title"][data["title"].str.contains("Python", case=False, na=False)])