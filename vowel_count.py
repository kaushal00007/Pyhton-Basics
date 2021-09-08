import pandas as pd
import numpy as np

#sentence ="my name is kaushal ooooo"
#vowel = ['a','e','i','o','u']
#words = sentence.split()
#vowel_count = {}
#for word in words:
#    for letter in word:
#        if letter in vowel:
#            vowel_count[letter] = word
#print ( vowel_count)
sentence = "ajay is rnnung a tech company which is specialized in tech visit ajay tech"
words = sentence.split()
my_dict = {}
for word in words:
    if my_dict.get(word) == None:
        my_dict[word] = 1
    else:
        my_dict[word] = my_dict[word] + 1
l_word_lenght =[]
for word in my_dict.keys():
    l_word_lenght.append([word,my_dict.get(word)])

def sort_criteria(ls):
    return ls[1]
l_word_lenght.sort()
l_word_lenght.sort(key = sort_criteria, reverse=True)
print(my_dict)
print(l_word_lenght)
#print(l_word_lenght.sort(),reverse = True)
