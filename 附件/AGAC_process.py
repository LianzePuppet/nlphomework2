# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 8:18
# @Author  : Deng Qidong
# @FileName: AGAC_process.py
# @Software: PyCharm
#读取AGAC语料库文件代码：

import os
import random
title=list()
text=list()
n=0
folder_path='E:/Desktop/大三下/NLP/作业1/AGAC_corpus/AGAC_training/txt'
folder_list = os.listdir(folder_path)
writefile=open("E:/Desktop/大三下/NLP/作业1/AGAC_abstract.txt","w+",encoding='utf-8')
for  folder in folder_list:
    new_folder_path = os.path.join(folder_path, folder)  # 根据子文件夹，生成新的路径   path.join 为前面的folder_path+后面的folder  例如：C:\CHE\+ 1.txt = C:\CHE\1.txt  即遍历后获取每个txt文件的绝对路径
    with open(new_folder_path, 'r', encoding='utf-8') as f:  # 打开该目录下的每一个文件
        i=0
        for eachline in f:
            #print(eachline)
            i=i+1
            if i!=1:
                writefile.write(eachline)

f.close()

'''
下面代码弃用，因为发现AGAC有很多文献并非两行式
n=n+1
    with open(new_folder_path,'r', encoding='utf-8') as f:#打开该目录下的每一个文件
        content = f.readlines()#读取其中的内容，返回一个列表，列表第一个元素是标题，第二个元素是内容
        #print(content)

        if len(content)!=2:
            print(folder)
            print(n)
            print(len(content))
        #title.append(content[0])
        #text.append(content[1])
    f.close()
'''
