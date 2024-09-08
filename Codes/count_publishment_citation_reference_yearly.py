import pandas as pd
from collections import defaultdict as dict
import numpy as np 

df = pd.read_csv("data from scopus.csv")

def return_0():
    return 0

publication_count = dict(return_0) 
citations_count = dict(return_0) 
references_count = dict(return_0)


for index, row in df.iterrows():
    year, citations, references = row["Year"], row["Cited by"], row["References"]
    publication_count[year] += 1
    citations_count[year] += 0 if pd.isna(citations) else citations
    references_count[year] += 0 if pd.isna(references) else len(references.split(";"))
    
for year in list(citations_count.keys()):
    citations_count[year] /= publication_count[year]
    references_count[year] /= publication_count[year]



table = np.zeros((len(citations_count.keys()),4))
for index, year in enumerate(citations_count.keys()):
    p = publication_count[year]
    c = citations_count[year]
    r = references_count[year]
    table[index,:] = [year,p,c,r]
df = pd.DataFrame(table)
df.to_excel("publishment_citation_reference_yearly.xlsx")



# # print(references_count)

# import matplotlib.pyplot as plt


# def plot_helper(data:list,xlabel:str,ylabel:str,title:str,figure_name:str):
#     """@data: [(x,y,label),]"""
#     fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
#     for x,y,lab in data:
#         ax.bar(x, y, label=lab)  
#     ax.set_xlabel(xlabel)  # Add an x-label to the axes.
#     ax.set_ylabel(ylabel)  # Add a y-label to the axes.
#     ax.set_title(title)  # Add a title to the axes.
#     ax.legend();  # Add a legend.
#     fig.savefig(figure_name)

# # print(citations_count)

# plot_helper( [(citations_count.keys(),citations_count.values(),"citation average")],"year","paper","citations average v.s. year","citations")
# plot_helper( [(publication_count.keys(),publication_count.values(),"publication")],"year","paper","publication v.s. year","publication")
# plot_helper( [(references_count.keys(),references_count.values(),"references average")],"year","paper","references average v.s. year","references")