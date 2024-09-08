import pandas as pd

def find_countries(s:str):
    s = s.split(';')
    countries = [a.split(',')[-1] for a in s]
    countries = [c.strip() for c in countries]
    return list(set(countries))


df = pd.read_csv("data from scopus.csv")

country_year_count = dict()
country_year_count["China"] = {y:0 for y in range(1995,2025)}

missing = 0

# only for test
counter_1 = 0
counter_2 = 0

for index, row in df.iterrows():
    affiliations = row["Affiliations"]
    if isinstance(affiliations,float):
        missing += 1
        continue
    countries = find_countries(affiliations)
    year = row['Year']
    for c in countries:
        if c in ["China","Taiwan","Hong Kong","Macao"]:
            continue
        if c not in country_year_count.keys():
            country_year_count[c] = {y:0 for y in range(1995,2025)}
            country_year_count[c][year] += 1
        else: # c in country_year_count.keys()
            country_year_count[c][year] += 1 
    if "China" in countries or "Taiwan" in countries or "Hong Kong" in countries or "Macao" in countries:
        country_year_count['China'][year] += 1


for c in country_year_count.keys():
    country_year_count[c]['sum'] = sum([country_year_count[c][y] for y in range(1995,2025)])
    country_year_count[c]['part_sum'] = sum([country_year_count[c][y] for y in range(1995,2005+1)])

print("The information of the following consitution is missing: ", missing)


headers = ["country","1995-2005",] + [str(y) for y in range(2006,2025)]  + ["sum"]

rows = []  


for key, value in country_year_count.items():  
 
    rows.append([key, value['part_sum']]+[value[y] for y in range(2006,2025)]+[value['sum']])  

df = pd.DataFrame(rows, columns=headers)  
df = df.sort_values(by='sum',ascending=False)

df.to_excel('country_publish_count.xlsx',index=False)

