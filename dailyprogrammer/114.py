import requests

def neighbor(a, b):
    return sum(1 for x,y in zip(a, b) if x==y) == 3

def all_neighbors(words, target):
    return [w for w in words if neighbor(w, target)]

words = requests.get('http://pastebin.com/raw.php?i=zY4Xt7iB').text.split()
word_map = {w: all_neighbors(words, w) for w in words}
