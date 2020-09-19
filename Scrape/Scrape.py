from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
for url in
my_url = "https://www.footballdb.com/stats/teamstat.html?lg=NFL&yr=2020&type=reg&cat=T&group=D&conf="

uClient = uReq(my_url)
page_html = uClient.read()
Html_file= open("","w")
Html_file.write(html_str)
Html_file.close()
uClient.close()

page_soup = soup(page_html, 'html.parser')
