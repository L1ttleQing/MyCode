import jieba
import wordcloud
import re
import requests

# 获取url
url = input("url = ")
headers = {
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
}

# 接收数据 整理编码
response = requests.get(url)
response.encoding = response.apparent_encoding

# 保存弹幕数据
o_data = response.text
o_list = re.findall('<d p=".*?">(.*?)</d>', o_data )
o = '\n'.join(o_list)
print(o)
with open('弹幕.txt',mode = "w",encoding='utf-8') as f:
    f.write(o)

# 定义函数，防止无意义词刷屏
def get_stopwords():
    stopwords = set()
    f = open("stopwords.txt", encoding="utf-8")
    line_contents = f.readline()
    while line_contents:
        line_contents = line_contents.replace("\n", "").replace("\t", "").replace("\u3000", "")
        stopwords.add(line_contents)
        line_contents = f.readline()
    return stopwords

# 生成词云
f = open("弹幕.txt",encoding= "utf-8")
txt = f.read()
string = ' '.join(jieba.lcut(txt))
wc = wordcloud.WordCloud(
    font_path="msyh.ttc",
    scale=15,
    stopwords=get_stopwords()
)
wc.generate(string)
wc.to_file("词云.png")

print("词云生成完毕！")

