
# def goodDay(name,ending="thank you"):
#     print(f"Hello, {name}!")
#     print(ending)

# goodDay("Annas","no thanks")
# goodDay("Bilal")

# def factorial(n):
#     if n==0 or n==1:
#       return 1
#     else:
#        return n*factorial(n-1)

# kk=int(input("enter the no for factorial: "))
# vv=(factorial(kk))
# print(f"the factorial is : {vv}")

# def f_to_c(f):
#    return 5*(f-32)/9       

# temp=(f_to_c(100))
# print(round(temp,2))

def rem(l,word):
    n=[]
    for item in l:
        if not (item==word):
          n.append(item.strip(word))
     
    return n

l=["annas","ali","raza","jamal"]
print(rem(l,"an"))