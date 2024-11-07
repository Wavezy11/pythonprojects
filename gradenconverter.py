import string
import random


print("Welkom gebruiker, hier kan je zien hoeveel graden of fahrenheit het is en omzetten.")

answer = input("Kies graden/fahrenheit")

#verschil tussen print en print(f"") is dat je geen variabelen in de normale print kan gebruiken in vergelijking met print(f "")

if answer.lower() == "graden":
    aantalGraden = float(input ("Hoeveel graden willen we omzetten vandaag?"))
    fahrenheit = (aantalGraden * 9/5) + 32
    print (f"Het is nu {fahrenheit}")
elif answer.lower() == "fahrenheit":
    aantalFahrenheit = float(input ("Hoeveel Fahrenheit wil je omzetten vandaag?"))
    celsius = (aantalFahrenheit - 32) * 5/9
    print (f"Het is nu {celsius}")
else:
    print("ongeldig")

