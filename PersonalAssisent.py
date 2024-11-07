import string
import random
from playsound import playsound 

# Start interaction
start = input("Hey Farhan, how are you doing? (Good/Bad): ")

if start == "Good":
    print("Nice to hear! What do you want to do right now?")
    begin_with_music = input("Would you like to listen to some music? (yes or no): ")
    
    if begin_with_music.lower() == "yes":
        sound_file = 'sounds/goodmorning.mp3'
        playsound(sound_file)
    elif begin_with_music.lower() == "no":
        print("Well, you having a bad day. No music either bruh")
elif start == "Bad":
    print("That's not nice to hear. Can I make it better for you?")
else:
    print("I didn't understand that response. Please answer with 'Good' or 'Bad'.")
