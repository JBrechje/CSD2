#Een functie die het type van het argument print

#en die een lijst met timestamps returned 
#die geconstrueerd is door de in note_durations waarden op basis van het bpm om te rekenen naar de juiste timestamp.
#Een functie die je een lijst mee geeft met namen van sample packs en die deze voorlegt aan de gebruiker, vervolgens 
#de gebruiker een keuze laat maken en de index van de desbetreffende keuze uit de lijst returned.
import pygame
import time

noteAmount = input("enter number of notes:")

bpm = float(input("enter bpm: "))
print("entered bpm:", bpm)

quarternote_dur = 60.00 / bpm
print("quarter note:", float(quarternote_dur))




note_durations = list()

for i in range(int(noteAmount)):
    note_durations.append(float(input("Enter note duration:")))

print("note_durations:", note_durations)


#def my_function(note_durations, bpm):
#  print("notes:", note_durations + " " + "bpm:", bpm)

#my_function("note_durations", bpm)



## ___ play rhythm ___
## init  mixer module and load sample
pygame.init()
sample = pygame.mixer.Sound('../assets/plop.wav')
sample.play()


# transform note durations to sequence of time durations (sec)
time_durations = []
for note_dur in note_durations:
    time_durations.append(quarternote_dur * note_dur)

print("time_durations", time_durations)


## play sequence
## TODO loop through time durations ans play sample
## use sample.play and time.sleep
for time_dur in time_durations:
    sample.play()
    time.sleep(time_dur) #wacht de tijd duratie voor ie opnieuw begint

## ensure sample playback is finished
time.sleep(sample.get_length())
