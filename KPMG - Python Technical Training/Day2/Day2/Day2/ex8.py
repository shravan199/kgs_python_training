# How to create a string object in python 
obj="Google News is a news aggregator service developed by Google. It presents a continuous flow of links to articles organized from thousands of publishers and magazines. Google News is available as an app on Android, iOS, and the Web. Google released a beta version in September 2002 and the official app in January 2006."
# break above str object into multine in code file only 
#output i want same as old one (one line)

obj="Google News is a news aggregator service developed by Google. \
It presents a continuous flow of links to articles organized from \
thousands of publishers and magazines. Google News is available as \
an app on Android, iOS, and the Web. Google released a beta version \
in September 2002 and the official app in January 2006."
print(obj)

#covert these text into str object and print it
a="This is Nishant's House."
print(a) 
a='This is "Nishant\'s" House.'
print(a) 
a='This is "Nishant" House.'  
print(a) 


#covert below multiline text into str object  and print output as  multiline ?

obj="Google News is a news's aggregator service developed by Google. \n\
It presents a continuous flow of links to articles organized from \n\
thousands of publishers and \"magazines\". Google News is available as \n\
an app on Android, iOS, and the Web's'. Google released a beta version \n\
in September 2002 and the official app in January 2006."

print(obj)



obj="""Google News is a news's "aggregator" service developed by Google. 
It presents a continuous's flow of links to articles organized from 
thousands of publishers and "magazines". Google News is available as 
an app on Android&$_, iOS, and the Web's'. Google released a beta version 
in September 2002 and the official app in January 2006."""
print(obj)

# row string
obj=r"C:\Users\OM\eclipse-workspace\tpmgAug2023\Day2"
print(obj)


