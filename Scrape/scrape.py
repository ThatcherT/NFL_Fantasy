from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import pickle
# import sys
# sys.setrecursionlimit(2500)
years = [2015, 2016, 2017, 2018, 2019, 2020]
first_year = years[0]
groups = ['O', 'D']
first_group = groups[0]
# years = [2015]
# groups = ['O']
i = 0
#iterating through multiple years of play, offense and defense
for year in years:
    for group in groups:
        my_url = f"https://www.footballdb.com/stats/teamstat.html?lg=NFL&yr={year}&type=reg&cat=T&group={group}&conf="

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, 'html.parser')
        table = page_soup.table
        # print(table)
        # print(table.find_all('th'))
        headers = []
        for th in table.find_all('th'):
            headers.append(th.text) #titles
        table_values = table.find_all('td') #a list of all values in table
        print(table_values)
        iter = 0
        inner_list = []
        outer_list = []
        teams = []
        for val in table_values: #each row
            if iter == 0:
                teams.append(val.a.text)
                inner_list.append(val.a.text)
            else:
                inner_list.append(val.text)

            if iter == 9:
                iter = -1
                outer_list.append(inner_list)
                inner_list = []
            iter += 1
        YEAR = [year for i in outer_list]
        if group == 'O':
            side = 'Offense'
        else:
            side = 'Defense'
        GROUP = [side for i in outer_list]
        if year == first_year and group == first_group:

            df = pd.DataFrame(outer_list, columns = headers)
            df['Year'] = YEAR
            df['Side'] = GROUP
        else:
            df2 = pd.DataFrame(outer_list, columns = headers)
            df2['Year'] = YEAR
            df2['Side'] = GROUP
            df = df.append(df2)

        # print(row_list[0].text)
        # with open(f'{year}_{group}', 'wb') as handle:
        #     pickle.dump(table,handle)
        # Html_file= open(f"{year}_{group}","w")
        # x = soup.find_all('table', class_='table-scroller')
        # print(x)
        # print(type(x))
        # Html_file.write(page_soup)
        # Html_file.close()
        i+=1

print(df)
df.to_pickle('./Historical.pkl')