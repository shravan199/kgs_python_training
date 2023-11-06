import requests as rq
import time
url="https://github.com/xpn/CUDA-MD5-Crack/raw/master/wordlist.txt"
res=rq.get(url)
print(type(res))
print(res.ok)



if res.ok:
    obj=open("out.txt",'wb')
    for chunk in res.iter_content(10000):
        obj.write(chunk)
        #print(chunk)
#         time.sleep(10)
#     obj.write(res.content)
    print("done")
else:
    print("URL not found!")
    