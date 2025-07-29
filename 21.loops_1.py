
# i=1
# while (i<6):
#    print(i)
#    i=i+1

for i in range (1,3):
   print(i)

l=["annas","raza", 'ali',True,3.34,1]
 
for i in l:
  print(i)

for i in range (1,5,2):
   print(i)
else:
   print("loop ended")  # This will print "loop ended" because the loop ended normally
i="hello"
for i in l:
    print(i)
    pass  # This pass statement does nothing but is syntactically required
    if isinstance(i, str):
        pass  # Placeholder for future string handling logic
    else:
        print(f"Non-string item: {i}")
    

    
    #factorial
n=int(input("enter the number : "))
f=1
for i in range (1,n+1):
       f=f*i
    
print(f"factorial of {n} is {f}")