import pandas as pd

df = pd.read_csv("data from scopus.csv")

journal_year_count = dict()

for index, row in df.iterrows():
    journal = row["Source title"]
    if isinstance(journal,float):
        print(row['Title'])
        continue
    year = row['Year']
    if journal not in journal_year_count.keys():
        journal_year_count[journal] = {y:0 for y in range(1995,2025)}
    else:
        journal_year_count[journal][year] += 1 

for j in journal_year_count.keys():
    journal_year_count[j]['sum'] = sum([journal_year_count[j][y] for y in range(1995,2025)])


headers = ["journal","sum",] + [str(y) for y in range(1995,2025)]  

rows = []  

  
for key, value in journal_year_count.items():  

    rows.append([key,value['sum']]+[value[y] for y in range(1995,2025)])  

df = pd.DataFrame(rows, columns=headers)  

df.to_excel('journal_publish_count.xlsx')

