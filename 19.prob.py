# s1={"kaam":"work","dukan":"shop"}
# s=input("enter what you want to search: ")
# print(s1.get(s))

# a=set()

# a1=int(input("enter your no: "))
# a.add(a1)
# a2=int(input("enter your no: "))
# a.add(a2)
# a3=int(input("enter your no: "))
# a.add(a3)
# print(a)


# s2d={44,"44"}
# # print(sd)

# set={1,1.0,'1'} #in python 1=1.0
# print(set)

d={}
name=input("enter the name : ")
lang=input("enter the language: ")
d.update({name:lang})
name=input("enter the name : ")
lang=input("enter the language: ")
d.update({name:lang})
name=input("enter the name : ")
lang=input("enter the language: ")    #agr same name ho tou jo pehle name likhe udr update hota
d.update({name:lang})

 

print(d)
