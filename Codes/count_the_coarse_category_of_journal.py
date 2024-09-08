import pandas as pd
import os 
import re
from collections import defaultdict


df = pd.read_excel("category_count.xlsx")


def return0():
    return 0
    
categories_count = defaultdict(return0)

def main():
    for index, row in df.iterrows():
        cat = row['category']
        cat = re.split(',',cat)[0]
        cat = cat.strip()
        categories_count[cat] += row['count']

    df2 = pd.DataFrame(categories_count.items())
    df2.to_excel("category_count_reduced.xlsx",header=["category","count"])


if __name__ == '__main__':
    main()