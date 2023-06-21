n = int(input())

word = []
for _ in range(n):
    word.append(input())
    
word = list(set(word))

result = []

for i in word:
    result.append((len(i),i))
result = sorted(result)

for _, word in result:
    print(word)