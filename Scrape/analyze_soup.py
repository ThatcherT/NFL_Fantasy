from Scrape import page_soup
table = page_soup.find_all('table', class_ = 'statistics scrollable')
print(table)