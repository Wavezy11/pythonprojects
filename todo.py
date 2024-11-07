userData = []

# Voeg items toe aan de lijst
while True:
    data = input("Voer je to-do item in (of typ 'stop' om te eindigen): ")
    if data.lower() == 'stop':
        break
    userData.append(data)

# Laat de gebruiker items verwijderen
while True:
    remove_item = input("Typ het item dat je wilt verwijderen (of typ 'klaar' om door te gaan): ")
    if remove_item.lower() == 'klaar':
        break
    if remove_item in userData:
        userData.remove(remove_item)
        print(f"{remove_item} is verwijderd.")
    else:
        print(f"{remove_item} is niet gevonden in de lijst.")



# Print de uiteindelijke to-do lijst
print("Je to-do lijst:")
for item in userData:
    print("- " + item)


# Opslaan naar een tekstbestand
with open('todo_list.txt', 'w') as file:
    for item in userData:
        file.write(item + '\n')  # Schrijf elk item op een nieuwe regel
