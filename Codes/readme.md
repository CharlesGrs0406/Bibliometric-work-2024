[crawler.py](./crawler.py) # This python script crawl the information of given journal names from Clarivate, like categories and abbreviations. All filed crawled from Clarivate should be used for academic research only.

[find_the_categories_of_journal.py](./find_the_categories_of_journal.py) # This python script extract the categories of each journal from the raw crawled *.csv file. Particularly, a journal may have different categories under different criteria.

[count_the_coarse_category_of_journal.py](./count_the_coarse_category_of_journal.py) # The original categories from Clarivate have too high level of granularity. This python script extract the coarse categories(of our interest) from the original ones. For example, it extracts "COMPUTER SCIENCE" from "CEOMPUTER SCIENCE, INFORMATION SYSTEMS".

[count_category_publishment.py](./count_category_publishment.py) # This python script calculates the total publication of the journals contained in each category. Moreover, it is also used to plot the the bar chart representing publishment across categories among predominant journals, i.e., Fig3 (a), the wordcloud generated from journal categories, i.e., Fig3(b) as well as the bar chart representing publishment across categories of all journals, i.e., Fig2 in supplementary materials.

[count_country_publishment_yearly.py](./count_country_publishment_yearly.py) # This python script calculates the yearly publication of each country staring from 1995. Notice that **the publication of China** include that of Hongkong, Macao and Taiwan. 

[count_H_SCP_MDP_of_country&constitute.ipynb](./count_H_SCP_MDP_of_country&constitute.ipynb)  # This Jupyter notebook calculates the publishment, SCP, MCP, total citations, H-index of all countries, calculates the publication, total reference, average reference and H-index of every constitutes and calculate the top10 productive authors' H-index.

[count_journal_publishment_yearly.py](./count_journal_publishment_yearly.py) # This python script calculates the yearly publication of each journal starting from 1995.

[count_journal_publishment_overall.py](./count_journal_publishment_overall.py) # This python script sums up the total publication of each journal starting from 1995.

[count_publishment_citation_reference_yearly.py](./count_publishment_citation_reference_yearly.py) # This python script calculates the publication, citation and reference of each year among our collected journals starting from 1995.

[extract_author_information.py](./extract_author_information.py) # This python file is used to extract the information of authors, like their IDs, full names,publication and citations.

[line_chart_top10_journals_across_year.R](./line_chart_top10_journals_across_year.R) # This R script is used to plot the line chart representing publication across years of the top 10 journals, i.e., Fig3 (c).

[line_chart_top10_proceedings_across_year.R](./line_chart_top10_proceedings_across_year.R) # This R script is used to plot the line chart representing publication across years of the top 10 proceedings, i.e., Fig3 (d).

[stacked_bar_chart_publication_across_year_among_countries.R](./stacked_bar_chart_publication_across_year_among_countries.R) # This R script is used to plot the stacked bar chart representing publication across year among countries, i.e., Fig5 (a).