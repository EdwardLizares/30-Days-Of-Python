import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(t):
    pattern = r'[%@#$&;!]'
    return re.sub(pattern, '', t)

def most_frequent_words(t):
    count = {}
    for i in re.findall(r'\b\w+\b',t):
        if i not in count:
            count[i] = 0
        count[i] += 1
    return list(reversed(sorted([(c, w) for w, c in (count.items())])[-3:]))

if __name__ == "__main__":
    print("1:", clean_text(sentence))
    print("1:", most_frequent_words(clean_text(sentence)))
