import requests as rq 
payload={"username":"Nishant","password":"YoYoNishant"}
req=rq.post("http://httpbin.org/post",data=payload)
print(req.text)