import string


# klantenregistratie
# Verzamel eerst hun info


print("Welkom in onze registratie")


username = str(input("Voer hier je naam in"))
email = str(input("Voer hier je E-Mail in"))
telnummer = str(input("Voer hier je telnummer in"))


## Opslaan in een tekstbestand
with open("klantenregistratie.txt", "a") as file:
    file.write(f"Naam: {username}, E-Mail: {email}, Telefoonnummer: {telnummer}\n")

print("\nRegistratie voltooid! Hier zijn de details die je hebt ingevoerd:")
print(f"Naam: {username}")
print(f"E-Mail: {email}")
print(f"Telefoonnummer: {telnummer}")