import requests as rq 
from bs4 import BeautifulSoup
from openpyxl import Workbook
url="https://www.imdb.com/search/title/?title_type=tv_movie&release_date=2022-01-01,2023-08-18&sort=release_date,asc&count=250"
res=rq.get(url)
soup=BeautifulSoup(res.content,'html.parser')
print(res.ok)
content=soup.find_all('div',class_="lister-item-content")
movies=list()
for item in content:#value
    name=item.h3.a.text
    try:
        rating= float(item.strong.text)
    except:
        rating=0
#     print(rating)
    movies.append((name,rating))
print(len(movies))
##########write a data into excel################
wb=Workbook()
sheet=wb.active
sheet.title="IMDB Movies Data"
sheet['A1']="Name"
sheet['B1']="Rating"
for movie in movies:
    sheet.append(movie)
    
wb.save("movies-18-08.xlsx")


#years
#votes(?)
#genre
#Director






