# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:28:54 2018

@author: Vinay Verma Coder's Mine
"""

file=open("essay.txt",'r')
#print(file.read())
lines=file.read()
#print(lines)
lines=lines.replace('.','\n')
#print(lines)
file.close()


file=open("Modified.txt",'w')
file.write(lines)
file.close()


file=open("converted.txt",'r')
#print(file.read())
lines=file.readlines()
#print(lines)
"""
now the essay is in list just like reviews 

"""

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

"""
if we remove the space also in this replace argument 
then it will replace the spaces in the sentence with nothing 
and hence messing up the whole sentence

"""
corpus=[]
for i in range(len(lines)):
    short=re.sub('[^a-zA-Z]',' ',lines[i])
    short=short.lower()
    short=short.split()
    ps = PorterStemmer()
    short=[ps.stem(word) for word in short if not word in set(stopwords.words('english'))]
    short=' '.join(short)
    corpus.append(short)

corpus=' '.join(corpus)
file=open('ShortedEssay.txt','w')
file.write(corpus)
file.close()
"""
finally done 
all the values are preserved and the other stupid words are removed 
the important words are present only which makes some things clear about the essay or article
making us to focus on important things only and discarding other stuffs
"""
