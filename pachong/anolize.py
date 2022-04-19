import jieba
from wordcloud import WordCloud
with open ('123.txt','r',encoding= 'utf-8')as file:
    word = file.read()

wordlist = jieba.lcut(word)
print(wordlist)

qwertylib = {}

for i in wordlist:
    if len(i)>1:
        if i in qwertylib:
            qwertylib[i]=qwertylib[i]+1
        else:
            qwertylib[i]=1

for num in qwertylib:
    if qwertylib[num]>20:
        print(num)