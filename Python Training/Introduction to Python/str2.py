a= "  thiS iS ShravaN kUMar jhA       "
print(a, type(a), id(a), len(a))

a = a.strip()
print(a, type(a), id(a), len(a))

b= a.capitalize()

print(b, type(b), id(b), len(b))


b= a.lower()

print(b, type(b), id(b), len(b))


d = "3454354545454"
print(f"Is string having digit characters: {d.isdigit()} ")

e = "dfdfdaeetetrt"
print(f"Is string having alpha characters: {e.isalpha()} ")

d = "5454dfda"
print(f"Is string having printable characters: {d.isprintable()} ")

f = "I am testing this code "
print(f"Is string ends with 'code' word: {f.strip().endswith('Code')}")



f = "I am testing this code "
print(f"Is string ends with 'code' word: {f.strip().endswith('Code')}")


xy = 'This is First time'
print(f'word fi present in given string: {xy.__contains__("fi")}')