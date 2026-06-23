#Data Types 

#Text Types
# string - str
# a= "Akash" , 'Aaksh' (you can provide single qutation or double quatiton)
#Numerical Types
# a= 123 - Integer (int)
# a= 23.78 Float (float)
# a = i + 3j complex (complex)
#Boolen Types
# a= True , False (bool)
# Squence Types
# a = ["item1","item2","item3"] : [1,23,4,5,5] - (list)
# a = ("item1","item2") : (2,4,6,79,0) - (tuple)
# Mapping Types
# a = {"name":"akash","age":27,"city":"Bangalore"} - (dict)
# Set Types
# a = {3,56,7,86,5,67}  - (set)
# a = frozenset{3,45,6,77,88} - (frozenset)

a= ["item1","item2","item3" ,"item1","item1"]
print(id(a))
print(a)

a.append("item4")
print(a.count("item1"))


b = ("item1","item2","item3" ,"item1")
print(b)
print(a)
print(b.count("item1"))
 

