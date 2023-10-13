# read() - nolasa visu datni
       #datne=open('info1.txt', encoding='utf-8')
    #print(datne.read())
# Nolasīt 2 reizes 5 simbolus
  #datne=open('info1.txt', encoding='utf-8')
  #print(datne.read(5))
  #print(datne.read(5))
# Nolasīt 2 reizes 5 simbolus, atrast nullto simbolu un nolasīt vēlreiz 5 simbolus
"""
datne=open('info1.txt', encoding='utf-8')
print(datne.read(5))
datne.seek(0)
print(datne.read(5))
"""
# Izdrukāt kursora atrašanās vietu
"""
datne=open('info1.txt', encoding='utf-8')
print(datne.read(5))
datne.seek(0)
print(datne.read(5))
pos=datne.tell()
print(f"Kursors atrodas {pos} pozīcijā")
datne.seek(0)
print(f"Kursors atrodas {datne.tell()} pozīcijā")
"""

# Ielasīt un izdrukāt visu datni, salīdzināt abas rindas (Enter ir (\n))
"""
datne=open('info1.txt', 'r',encoding='utf-8')
viss=datne.readlines()
print("viss=", viss)
"""
# Nolasīt un izdrukāt abas rindas
"""
datne=open('info1.txt', 'r',encoding='utf-8')
print(datne.readline(), end="")
print(datne.readline(), end="")
"""

# Nolasīt visu datni ciklā un aizvērt datni
datne=open('info1.txt', 'r',encoding='utf-8')
for rinda in datne:
    print(rinda, end="")
datne.close()

