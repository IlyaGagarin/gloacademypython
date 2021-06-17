# -- coding: utf-8 
nametekst1 = input()
nametekst2=input()
nametekst3=input()
if len(nametekst1)>len(nametekst2) and len(nametekst1)>len(nametekst3):
    print (nametekst1)
elif len (nametekst2)>len(nametekst1) and len (nametekst2)> len (nametekst3):
    print (nametekst2)
else:
    print (nametekst3)