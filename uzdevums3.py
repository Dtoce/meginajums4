# Atveru 'info1.txt' ar 'a' , lai pieliktu (append) 
# izsaucu funkciju nolasaDrukaDatni(), kura 
# nolasa ‘info1.txt’un izdrukā tās saturu


with open('info1.txt', 'a', encoding="utf-8") as datne: 
    datne.write('Piektdiena ir klāt! \n')
    

     