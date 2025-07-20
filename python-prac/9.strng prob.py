# a="this is practice broo"

# bs=input("enter the bullshit: ")
# print(f"this is what i entered {bs}")
#triple quote for as it is lines
letter='''dear <|Name|>
you are selected
<|Date|>
'''

print(letter.replace("<|Name|>","Annas").replace("<|Date|>","12-4-22"))

d="hello  is  double  spaced"
print(d.replace("  "," "))
#fucntion only creates new string the original remains the same(immutable strings)
print(d)