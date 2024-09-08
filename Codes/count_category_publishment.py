import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  
# import matplotlib
from wordcloud import WordCloud 

file_path = 'journal_category.xlsx'  
# file_path = 'journal_category.xlsx'
df = pd.read_excel(file_path)  

##################################################
################### Fig 3 (a) ####################
##################################################

# Find the predominant **journal** with publishment >= threshold
threshold = 3
filtered_df = df[df['count'] >= threshold]

# count the publishment of each category
category_counts = filtered_df.groupby('category')['count'].sum().reset_index()  
category_counts.columns = ['category', 'total_count']  
  
# sort the categories by publishment
category_counts_sorted = category_counts.sort_values(by='total_count', ascending=False)  
category_counts_sorted.to_excel("category_publish_count_among_predominant_journals.xlsx")

# select the category with publishment >= threshold2 
threshold2 = 0
filtered_category_counts = category_counts_sorted[category_counts_sorted['total_count'] >= threshold2]  

# barplot 
plt.figure(figsize=(15, 10))  
sns.barplot(x='total_count',y='category', data=filtered_category_counts)  

# label and title 
plt.xlabel('Count', fontsize=16, fontweight='bold', fontfamily='Arial')  # fontsize设置字号，fontweight设置加粗，fontfamily设置字体  
plt.ylabel('Categories', fontsize=16, fontweight='bold', fontfamily='Arial')  
plt.title(f'Bar Chart Representing Publishment Across Categories Among Predominant Journals', fontsize=18, fontweight='bold', fontfamily='Arial')  

plt.tight_layout()  
plt.savefig(f"Bar Chart Representing Publishment Across Categories Among Predominant Journals with publishment >= {threshold}.png")
# plt.show()


################################################
#################  Fig 3 (b)  ##################
################################################

categories = category_counts_sorted['category'].tolist() 
counts = category_counts_sorted['total_count'].tolist()  

# generating wordcloud
wordcloud = WordCloud(background_color='white',font_path='arial.ttf',max_font_size=300 ,max_words=200, width=2000, height=1200, prefer_horizontal=1)  
wordcloud.generate_from_frequencies(dict(zip(categories, counts)))  

plt.figure(figsize=(20, 12))  
plt.imshow(wordcloud, interpolation='bilinear')  
plt.axis('off')   
# plt.show()  
   
plt.savefig('wordcloud_journal_categories.png')


##################################################
############## Supplementary Fig 2 ###############
##################################################

category_counts = df.groupby('category')['count'].sum().reset_index()  
category_counts.columns = ['category', 'total_count']  
  
category_counts_sorted = category_counts.sort_values(by='total_count', ascending=False)  
category_counts_sorted.to_excel("category_publish_count.xlsx")

# find the predominant **category** with total publishment >= threshold
threshold = 1
filtered_category_counts = category_counts_sorted[category_counts_sorted['total_count'] >= threshold]  
  

plt.figure(figsize=(15, 10))  
sns.barplot(x='total_count',y='category', data=filtered_category_counts)  
plt.yticks(size=6)


plt.xlabel('Count', fontsize=16, fontweight='bold', fontfamily='Arial')  # fontsize设置字号，fontweight设置加粗，fontfamily设置字体  
plt.ylabel('Categories', fontsize=16, fontweight='bold', fontfamily='Arial')  

plt.title(f'Bar Chart Representing Publishment Across Journal Categories', fontsize=20, fontweight='bold', fontfamily='Arial')  


plt.tight_layout()    
plt.savefig(f"Bar Chart Representing Publishment Across Journal Categories with publishment >= {threshold} (Supp Fig2).png")
# plt.show()