
#by using the with statement we dont have to use the close statement
with open("file.txt") as f:
    data = f.read()
    print(data)