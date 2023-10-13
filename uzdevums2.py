menesi=["Janvāris", "31", "Februāris", "28", "Marts", "30"]

    
with open('info1.txt', 'w', encoding="utf-8") as datne: 
    for vards in menesi:
        datne.write(vards)
        datne.write(" ")
        
def nolasaUnIzdruka():
        datnee=open('info1.txt', 'r', encoding='utf-8')
        datii=datnee.readline()
        print(datii)
        
nolasaUnIzdruka()        