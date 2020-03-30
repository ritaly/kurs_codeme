with open("pantadeusz.txt", encoding='utf-8') as fopen:
    content = fopen.read()

content = content.split()
print(content)

max_word = ''
for word in content:
    if len(word) > len(max_word):
        max_word = word

print(max_word)