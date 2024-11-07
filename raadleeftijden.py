import datetime

naam = input("Wat is je naam? ")
print(f"Goedemiddag {naam}, vandaag kijken we hoe oud je bent!")

geboortedatum_str = input("Wat is je geboortedatum? (in de vorm dd-mm-jjjj): ")

geboortedatum = datetime.datetime.strptime(geboortedatum_str, "%d-%m-%Y")


huidige_datum = datetime.datetime.now()


leeftijd = huidige_datum - geboortedatum
leeftijd_jaren = leeftijd.days // 365  


print(f"Dus je bent {leeftijd_jaren} jaar oud.")
