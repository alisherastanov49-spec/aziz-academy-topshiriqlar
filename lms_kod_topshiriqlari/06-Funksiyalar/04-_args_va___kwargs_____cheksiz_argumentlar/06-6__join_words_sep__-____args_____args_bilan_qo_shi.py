def join_words(sep, *args):
    return sep.join(args)
sep = input().strip()
words = input().split()
print(join_words(sep, *words))