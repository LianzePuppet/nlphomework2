print("==========案例1：分句、分词===============")
import nltk.tokenize as tk
import os
import string
import re
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg
from  imageio  import imread
from wordcloud import WordCloud
import numpy as np
# Step 1: Data preprocessing.
def str_norm(str_list: list, punc2=' ', space2=' ', lower=True):
    punctuation = string.punctuation.replace('-', '')
    rep_list = str_list.copy()
    for index, row in enumerate(rep_list):
        row = row.strip()
        for pun in punctuation:
            row = row.replace(pun, punc2)
        if lower:
            row = row.lower()
        rep_list[index] = re.sub(' +', space2, row)
    return rep_list

def Data_Pre(corpus: str, out: str, head = True):
    if os.path.exists((out)):
        return out
    wf = open(out, 'w', encoding='utf-8')
    with open(corpus, encoding='utf-8') as f:
        if head:
            f.readline()
        for line in f:
            l = line.strip()
            sent_list = str_norm([l], punc2=' ', space2=' ')
            for sent in sent_list:
                wf.write('{0}\n'.format(sent))
    wf.close()
    return out
raw_file = 'E:/Desktop/NLP/作业1/AGAC_abstract.txt'
corpus = Data_Pre(raw_file, 'E:/Desktop/NLP/作业2/AGAC.txt')

text = open('E:/Desktop/NLP/作业2/AGAC.txt',encoding='utf-8').read()
'''
# 按句拆分:tk.sent_tokenize(text)
# 问：tk.sent_tokenize()为何能识别出到哪里是一句？
# 答：1、看首字母是大写 ；2、结尾有标点符号
tokens = tk.sent_tokenize(text)
#for i, token in enumerate(tokens):
    #print("%2d" % (i + 1), token)

print("-----------------------------")
'''

# 按词拆分:tk.word_tokenize(text)
tokens = tk.word_tokenize(text)
#print(len(tokens))
'''
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)



# 按词和标点拆分:tk.WordPunctTokenizer().tokenize(text)
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(text)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)


print("=============案例2：词干提取、词型还原===================")
'''
# 导入下面三种词干提取器进行对比
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb




print("----------词干提取-------------")
# 在名词和动词中，除了与数和时态有关的成分以外的核心成分。
# 词干并不一定是合法的单词

pt_stemmer = pt.PorterStemmer()  # 波特词干提取器
lc_stemmer = lc.LancasterStemmer()  # 兰卡斯词干提取器
sb_stemmer = sb.SnowballStemmer("english")  # 思诺博词干提取器
'''
for word in tokens:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print("%8s %8s %8s %8s" % (word, pt_stem, lc_stem, sb_stem))

'''

with open('AGAC_stem.txt', 'w',encoding='utf-8') as f:
    for word in tokens:
        sb_stem = sb_stemmer.stem(word)
        f.write(sb_stem+' ')
    f.close()




with open(r"AGAC_stem.txt", encoding="utf-8") as file_object:
    contents = file_object.read()

color_mask = imread("Deng.png")#建议图片背景颜色为白色
wordcloud = WordCloud(
    #font_path=r"C:\Windows\Fonts\Deng.tff",# 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    background_color="white",#设置背景颜色，建议设置白色
    width=1080,#设置宽度
    mask=color_mask,#设置背景图片，这里是大象
    height = 960)#设置高度

"""步骤三：生成词云图"""
wordcloud.generate(contents)#加载文本
wordcloud.to_file("Dengresult.png")#保存图片
plt.imshow(wordcloud)#背景图片
plt.show()

'''

text = open('AGAC_stem.txt').read()
import numpy as np
from PIL import Image

pic = np.array(Image.open("image.png"))

font = 'C:/Windows/Fonts/Deng.tff'
color_mask = imread(os.getcwd()+"\\xia.png")  # 读取背景图片
cloud = WordCloud(
 # 设置字体，不指定就会出现乱码
 font_path=font, #这个路径是pc中的字体路径
 # 设置背景色
 background_color='white',
 # 词云形状
 mask=color_mask,
 # 允许最大词汇
 max_words=2000,
 # 最大号字体
 max_font_size=40
)
word_cloud = cloud.generate(text)  # 产生词云,输入的格式是以空格分隔的词语组成的字符串
word_cloud.to_file("AGAC.jpg")  # 保存图片
#  显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()

#print("----------词型还原器---------------")
# 词型还原：复数名词->单数名词 ；分词->动词原型
# 单词原型一定是合法的单词


lemmatizer = ns.WordNetLemmatizer()
for word in words:
    # 将名词还原为单数形式
    n_lemma = lemmatizer.lemmatize(word, pos='n')
    # 将动词还原为原型形式
    v_lemma = lemmatizer.lemmatize(word, pos='v')
    print('%8s %8s %8s' % (word, n_lemma, v_lemma))


'''