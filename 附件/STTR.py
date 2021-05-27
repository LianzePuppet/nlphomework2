# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 1:07
# @Author  : Deng Qidong
# @FileName: STTR.py
# @Software: PyCharm
import random
import numpy as np

file_path1='./GENIA_abstract.pure.txt'
file_path2='./AGAC_abstract.pure.txt'

def read_and_cal_STTR(path,round=10000,size=1000):
    a=list()
    len_list=list()
    #path:文件路径 round：抽样次数 size：抽样个数
    with open (file_path1, 'r', encoding='utf-8') as f:
        for each_word in f:
            a.append(each_word)#存储每一个单词
        for i in range(round):
            resultList = random.sample(a,size) # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。上面的方法写了那么多，其实Python一句话就完成了。
            unique=set(resultList)
            len_list.append(len(unique))
            #print(len(unique))
        average_len = np.mean(len_list)*100/size
        print(average_len,'%')

read_and_cal_STTR(file_path1,10000,1000)
read_and_cal_STTR(file_path2,10000,1000)