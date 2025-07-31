# st=open("file.txt")
# s=st.readlines()
# #as a list output krega sare lines ko
# print(s)

# d=st.readline()
# print(d)

# d=st.readline()
# print(d)

# Open the file in read mode
st = open("file.txt")

# Read and print each line until the end of the file
s = st.readline()

while s != "":
    print(s)  # `end=""` prevents double newlines
    s = st.readline()

# Close the file after reading
st.close()
