freq = {}
for w in input().split():
    freq[w] = freq.get(w, 0) + 1
for w in sorted(freq):
    print(w, freq[w])