import sys, collections as c
words = c.Counter(sys.stdin.read().split())
for k in sorted(words):
    print(k, words[k])