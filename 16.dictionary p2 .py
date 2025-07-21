a={"annas":100,
   "ali":34,
   "shameer":44,
   0:"annas"}
print(a)

print(a.keys())
print(a.items())
print(a.values())
a.update({"annas":99,"javed":33})
print(a)

a.get("annasd")#return null
a["annasd"]#returns error


a.pop("ali")
print(a)


a.popitem()
print(a)