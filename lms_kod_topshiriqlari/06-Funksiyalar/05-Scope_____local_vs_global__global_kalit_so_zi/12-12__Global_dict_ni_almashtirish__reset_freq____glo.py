freq = {'a': 1}

def reset_freq():
    global freq 
    freq = {}
    
def add_word(word):
    global freq  
    freq[word] = freq.get(word, 0) + 1 
    
word = input().strip().lower()
reset_freq()
add_word(word)
print(freq)