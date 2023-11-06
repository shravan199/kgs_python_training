#string methods 
# a="      tHiS Is nIsHanT HOuse. Is is       "
# print(a,len(a),id(a))
# a=a.strip()#remove the whitespace chars from left & right side of your string#a.rstrip()#remove the whitespace from right side of your string #a.lstrip()#remove the whitespace from left side of your string
# print(a,len(a),id(a))
# b=a.replace("Is", "mm",2)#a.swapcase()#a.lower()#a.upper()#a.capitalize()
# print(b,len(b),id(b))

# a="niN1234@"
# print(a)
# 
# #b=a.isdigit() #Returns True if all characters in the string are digits
# # b=a.isalpha() #Returns True if all characters in the string are in the alphabet
# # b=a.isspace()#Returns True if all characters in the string are whitespaces
# # b=a.isupper()#Returns True if all characters in the string are upper case
# b=a.islower()#Returns True if all characters in the string are lower case
# print(b)

a="0y Kal jo na jo.Mp3"
print(a)
# b=a.endswith(".mp3")#Returns true if the string ends with the specified value
#b=a.startswith('01')#Returns true if the string starts with the specified value
b=a.__contains__('Ho')#Returns true if the string match the key 
print(b)











