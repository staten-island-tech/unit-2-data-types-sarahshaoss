animals = ["Zebra", "Camel", "Ape"]
#start count at 0, reference each element with brackets
print(animals[0])
for animal in animals:
    if(animal == "Camel"):
        print("We're in the desert")

#Strings operate like lists
x = "Hello Freshman, you all smell"

print(x[0]) 

y = x.upper()
print(y)

words_list = x.split(" ")
print(len(words_list))