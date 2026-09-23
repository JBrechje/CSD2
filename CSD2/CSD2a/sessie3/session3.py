from random import sample

import pygame
import time
import simpleaudio as sa

#een functie die het type van het argument print
def print_argument_type(argument):
    print("Het type van het argument is:", type(argument))

def greet_user():
  return "start your rhythm!"
message = greet_user()
print("system says; ", message)

###################################################################

#een functie die note_durations en bpm verwacht
#returned een lijst met timestamps
#vraag om user input

num_notes = input("Enter num notes\n") #vraag om user input
note_durations = list()

for i in range(int(num_notes)):
    note_durations.append(float(input("Enter note duration\n"))) #vraag om user input

print("note_durations:", note_durations) #returned een lijst met timestamps

#vraag bpm op & bereken quarternote
bpm = float(input("Enter BPM\n"))
quarternote_dur = 60.0 / bpm
print("bpm:", bpm, "quarternote_dur", quarternote_dur) #een functie die note_durations en bpm verwacht


#######################################################################

#een functie met een lijst met namen van sample packs 
#deze voorlegt aan gebruiker
#gebruiker een keuze laat maken 
#index van de keuze uit de lijst returned.


#sample options
def sample_options(sample_name): #een functie met een lijst met namen van sample packs 
    print("option 0: " + sample_name[0]) #deze voorlegt aan gebruiker
    print("option 1: " + sample_name[1])
    print("option 2: " + sample_name[2])


    #vraag om sample
    sample_choice = int(input("Enter prefered sample\n"))#gebruiker een keuze laat maken 

    return sample_name[sample_choice]  #index van de keuze uit de lijst returned.
    #gebruikt index om iets uit mijn lijst sample_name te halen


sample_name = ["dog", "plop", "drum"] #volgorde komt overeen met de nummers in []

sample_choice = sample_options(sample_name)

print("Sample:", sample_choice)