heros=['spider man','thor','hulk','iron man','captain america']

print("Length of the list: ", len(heros))
heros.append('black panther')
print("Added Black panther:",heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

#Removing thor & hulk & adding dr. strange
heros[1:3]=["Dr. strange"]
print(heros)

heros.sort() #Capital is preferred over small letters
print(heros)