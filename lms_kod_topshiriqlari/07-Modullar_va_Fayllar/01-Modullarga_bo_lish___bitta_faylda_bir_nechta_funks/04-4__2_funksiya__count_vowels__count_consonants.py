s = input()
def vowel(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
def con(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)
print(vowel(s))
print(con(s))