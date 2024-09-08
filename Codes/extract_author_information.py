import pandas as pd

def find_authors_id(s:str):
    print(s)
    return s.split(';')

def find_authors_full_names(s:str):
    return s.split(';')

df = pd.read_excel("data_from_scopus.xlsx")

authors = dict()

for index, row in df.iterrows():
    author_ids_str = row["Author(s) ID"]
    if isinstance(author_ids_str, float):
        print(row['Title'])
        continue
    author_full_names_str = row["Author full names"]
    author_ids = find_authors_id(author_ids_str)
    author_full_names = find_authors_full_names(author_full_names_str)
    for k in range(len(author_ids)):
        id = author_ids[k]
        if id not in authors:
            authors[id] = dict()
            authors[id]['full_names'] = author_full_names[k]
            authors[id]['publication'] = 1
            authors[id]['cited'] = row["Cited by"]
        else:
            authors[id]['publication'] += 1
            authors[id]['cited'] += row["Cited by"]


headers = ["ID", "full_names", "publication", "cited"] 

rows = []  

for key, value in authors.items():  
 
    rows.append([key,value['full_names'],value['publication'],value['cited']])  
 
df = pd.DataFrame(rows, columns=headers)  

df.to_excel('author_info.xlsx')