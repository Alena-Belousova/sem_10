#сколько неповторяющихся слов тексте
text='jingle bells jingle bells jingle all the way'
words=[]
words=text.split(' ')
print('исходный текст: ', words)
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print('строка без повторяющихся слов ',unique)
result = len(unique)
print(result)



