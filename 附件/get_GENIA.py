# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 19:46
# @Author  : Deng Qidong
# @FileName: get_GENIA.py
# @Software: PyCharm
with open("GENIA_abstract.pure.txt",'r', encoding='utf-8') as lines:
    with open ("get_part_of_GENIA.txt",'w', encoding='utf-8') as f:
        n=0
        for line in lines:
            print(line)
            if n<55414:
                f.write(line)
                n=n+1
        f.close()
        lines.close()
