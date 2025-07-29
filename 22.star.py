#print statement by default aik newline add krta ha
#end ="" likhne se iske agy se hi shuru hota
n=int(input("enter a no : "))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))