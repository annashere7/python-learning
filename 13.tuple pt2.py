#functions of tuple
a=("annas",33,True,4.23,33)
no=a.count(33)
print(no)

index=a.index(33)
print(index)        #hum new chez generate kr rahe orginal tuple same hi


#for repeeated tuple
b=("annas",33,True,4.23,33)
repeat=b*3
print(repeat)

print("annas" in b) #true

tt1=(3,2,5,2,6)
t1=(3,2,7)
print(t1+tt1)  #concate

#unpacking tuples
c,d,e=t1
print(c,d,e)  #3 2 7

o=sum(tt1)
print(o)
print(len(t1))