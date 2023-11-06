import bs4
#https://scrapy.org/
html="""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
   <title>My title</title>
</head>
<body>
This is just a text <br />
<p class='css1'>first paragraph </p>
<p id='myid'>second paragraph </p>
<p>third paragraph </p>
<br />
<a href="https://www.python.org" class='mylink'>first link</a><br />
<a href="http://www.linux.com">second link</a>
<a>second link</a>
<br />
<div class='some_class'>
   this is inside a div<br />
   <p>paragraph inside a div</p>
</div>

<div class='some_class1'>
   this is inside a div-1<br />
   <p>paragraph inside a div-1</p>
</div>

</body>
</html>

"""

soup=bs4.BeautifulSoup(html,"html.parser")

# g=soup.title.text
# print(g)
# b=soup.body.text
# print(b)
#m=soup.find('div')# return only first div tag
# m=soup.find_all('div')# list of all div tags
#m=soup.find_all(['div','p'])#return the list of all div and p tags
#m=soup.find_all('p',id='myid')
# m=soup.find_all('div',class_="some_class")
# print(m)
#print all the anchor tags ? 
b=soup.find_all('a',href=True,limit=10)
print(b)
for link in b:
    print(link.get('href'))









