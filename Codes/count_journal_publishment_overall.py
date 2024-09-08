import pandas as pd
from collections import defaultdict as dict
# from wordcloud import WordCloud  
# import matplotlib.pyplot as plt
import  numpy as np


df = pd.read_csv("data from scopus.csv")

def return_0():
    return 0

source_count = dict(return_0) 

for index, row in df.iterrows():
    source = row["Source title"]
    source_count[source] += 1

# source_count = sorted(source_count.items(),key=lambda t : t[1],reverse=True)

# print(source_count)

df = pd.DataFrame(source_count.items())
# table = np.zeros((len(source_count),2))
# for index, item in enumerate(source_count):
#     s,n = item
#     table[index,:] = [s,n]
# df = pd.DataFrame(table)
df.to_excel("results.xlsx",header=["source","count"])


# for index, row in df.iterrows():
#     source = row["Source title"]
#     source_word = source.split()
#     for w in source_word:
#         source_count[w] += 1

# years_list = list(range(2000,2025))
# years_list = map(str,years_list)

# index_list = list(range(3,50))
# index_list = map(lambda x: str(x)+"th", index_list)

# word_list = ["and","of","in","the","on","conference","lecture","proceedings","-","notes",
#              "workshop","journal","research","for","ieee","including","(including","acm","studies",
#              "conference,","plos","EMNLP"]

# word_list.extend(years_list)
# word_list.extend(index_list)
# word_list.extend(["1st","2nd"])

# for key in source_count.keys():
#     if key.lower() in word_list:
#         source_count[key] = 0

# # source_count = sorted(source_count.items(),key=lambda t : t[1],reverse=True)


