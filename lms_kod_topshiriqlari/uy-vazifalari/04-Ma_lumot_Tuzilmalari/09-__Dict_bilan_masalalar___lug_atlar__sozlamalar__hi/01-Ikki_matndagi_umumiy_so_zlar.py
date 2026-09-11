words1 = set(input().split())
words2 = set(input().split())
comman_words = sorted(words1 & words2)
for word in comman_words:
    print(word)