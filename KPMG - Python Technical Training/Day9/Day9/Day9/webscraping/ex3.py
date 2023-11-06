import requests as rq
import time

url="https://craphound.com/images/1006884_2adf8fc7.jpg"
#res=rq.get(url,headers={"Auth":"Token"})
res=rq.get(url)
print(res.status_code)
if res.ok:
    obj=open("out.png",'wb')
    for chunk in res.iter_content(10000):
        obj.write(chunk)
        #print(chunk)
#         time.sleep(10)
#     obj.write(res.content)
    print("done")
else:
    print("URL not found!")

# 127.0.0.1:8000/api/student
# 
# get the list of student > requests.get() 
# insert the student or students > requests.post()
# update the > put , patch 
# delete the > delete