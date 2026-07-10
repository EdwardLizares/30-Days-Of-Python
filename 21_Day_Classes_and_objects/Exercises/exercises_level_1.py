from collections import Counter
from functools import reduce
class Statistics():
    def __init__(self, data):
        self.data = sorted(data)
        self.freq_data = sorted([(v,k) for k,v in 
                                 list(dict(Counter(self.data)).items())], reverse=True)
    def count(self):
        return len(self.data)
    def sum(self):
        return reduce(lambda x,y: x+y, self.data)
    def min(self):
        return self.data[0]
    def max(self):
        return self.data[-1]
    def range(self):
        return self.data[-1]-self.data[0]
    def mean(self):
        return self.sum()/self.count()
    def median(self):
        return (self.data[(self.count()-1)//2]+self.data[self.count()//2])/2
    def mode(self):
        return dict(mode=self.freq_data[0][1], count=self.freq_data[0][0])
    def var(self):
        return sum((x-self.mean())**2 for x in self.data) / (self.count() - 1)
    def std(self):
        return self.var()**0.5
    def freq_dist(self):
        return self.freq_data

def test_statistics_class():
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 
            24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    data = Statistics(ages)
    print(data.data)
    print('Count:', data.count()) # 25
    print('Sum: ', data.sum()) # 744
    print('Min: ', data.min()) # 24
    print('Max: ', data.max()) # 38
    print('Range: ', data.range()) # 14
    print('Mean: ', data.mean()) # 30
    print('Median: ', data.median()) # 29
    print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
    print('Standard Deviation: ', data.std()) # 4.2
    print('Variance: ', data.var()) # 17.5
    print('Frequency Distribution: ', data.freq_dist())

if __name__ == "__main__":
    test_statistics_class()
