import sys
def words1(text):
    return text.split()
def word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        print(word(input_data))