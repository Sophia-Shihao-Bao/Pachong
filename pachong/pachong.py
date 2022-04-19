import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud
option1 = input('请输入您要爬取的内容，1.代表电影 2.代表图书')
option2 = input('请输入电影/图书的豆瓣ID号')
for num in range(0,20):
    url = 'https://movie.douban.com/subject/' + option2 + '/comments?start=' + str(20 * num) + '&limit=20&sort=new_score&status=P'
    url2 = 'https://book.douban.com/subject/' + option2 + '/comments/hot?p=' + str(num)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
    }
    print('正在搜索中，请稍后。。。')
    if option1 =='1':
        result = requests.get(url, headers=headers)
    elif option1=='2':
        result = requests.get(url2, headers=headers)
    soup = BeautifulSoup(result.content,'lxml')
    #print(soup)

    rewew = soup.find_all('span',class_ = 'short')
    for re in rewew:
        with open('refew.txt','a',encoding='utf-8')as file:
            file.write(re.get_text())
            file.write('\n')

with open ('refew.txt','r',encoding= 'utf-8')as file:
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
wc = WordCloud(
    font_path='youyuan.ttf',
    width=1000,
    height=1000,
    max_words=150,
    background_color='white'
)
wc.generate_from_frequencies(qwertylib)
wc.to_file('cloud.jpg')

