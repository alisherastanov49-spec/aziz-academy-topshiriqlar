def vol(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    is_vol = 1 if s[0] in vowels else 0
    return is_vol + vol(s[1:])
text = input().strip()
print(vol(text))