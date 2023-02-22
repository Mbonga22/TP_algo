
liste_voyelle = ['a','e','i','o','u']
def nbr_voy_et_conson(tab, n = 0):
    a = -1 if tab[n] in liste_voyelle else 1
    if n == len(tab)-1:
        return a
    else:
        return a+ nbr_voy_et_conson(tab, n +1)
 
def compt(tab):
    nbre = nbr_voy_et_conson(tab)
    if nbre>0:
        return "Dans ce cas, les consonnes sont plus nombreuses que les voyelles de ", nbre
    elif nbre<0:
        return " Dans ce cas, les voyelles sont plus nombreuses que les consonnes de ",abs(nbre)
    else:
        return "les consonnes sont autant que les voyelles"
 
les_mots = []
print("Taper les mots ")
for i in range(3):
    print("mot ",(i+1))
    
    a=input()
    les_mots.append(a)
for i in les_mots:
    print (compt(i), i)
