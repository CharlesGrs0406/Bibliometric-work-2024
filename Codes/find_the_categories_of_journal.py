import pandas as pd
import os 
import re
from collections import defaultdict


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def main():
    df = pd.read_excel("journals.xlsx")
    index_name = dict()
    journal_names = set()
    journal_categories = dict()
    for index, row in df.iterrows():
        index_name[row["source"].lower()] = index 
        journal_names.add(row["source"].lower())
        journal_categories[row["source"].lower()] = set()

    base = './journal_info/' # all the files crawled from Clarivate should be stored under this path
    for path in findAllFile(base):
        journal_info = pd.read_csv(path,header=1)

        for index, row in journal_info.iterrows(): # extract the category of the journal
            journal_name = index
            if isinstance(journal_name,str):
                journal_name = journal_name.lower()
            if  journal_name in journal_names:
                categoreis = row['eISSN']
                categoreis = re.split('-',categoreis)
                categoreis = list(map(lambda x: x.strip(), categoreis))[:-1]
                journal_categories[journal_name].update(categoreis)

    df['category'] = df['category'].astype(str)

    for journal_name in list(journal_names):
        index = index_name[journal_name]
        df.at[index,'category'] = ' ; '.join(journal_categories[journal_name])
        # print(df.at[index,'category'])

    df.to_excel("journal_category.xlsx", index=False)
                
    # count the category
    def return0():
        return 0
    categories_count = defaultdict(return0)
    for journal_name in list(journal_names):
        index = index_name[journal_name]
        for c in journal_categories[journal_name]:
            categories_count[c] += df.at[index,'count']
    df2 = pd.DataFrame(categories_count.items())
    df2.to_excel("category_count.xlsx",header=["category","count"])


if __name__ == '__main__':
    main()