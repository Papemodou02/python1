prix_ht= float(input("montant du prix ht:"))
# réduction de 15% si le prix dépasse 20000
if prix_ht>20000:
    prix_ht*=0.85 # équivalent à une réduction de 15%
# ajout de la TVA de 20%
prix_ttc= prix_ht *1.20
print("montant ttc à payer:", prix_ttc, "FCFA")
    
    
