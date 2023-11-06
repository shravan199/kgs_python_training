import requests as rq
url="https://www.python.org/"
output=rq.get(url)
print(type(output))
print(output.status_code)
print(output.ok)
content=output.content
print(content)
text_data=output.text
print(text_data)
