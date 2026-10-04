n = int(input())
st = []
for _ in range(n):
    name, score = input().split()
    st.append((name, int(score)))
st.sort(key=lambda s: -s[1])
for name, score in st:
    print(name, score)