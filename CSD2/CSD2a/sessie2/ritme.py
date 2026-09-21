#Werk daarna als volgt stap voor stap je script verder uit:
#'doorloop' deze lijst met behulp van een forloop (zie https://www.w3schools.com/python/python_for_loops.asp) 
#en print met behulp van deze forloop de waarden uit deze lijst
#importeer de time module en gebruik in de forloop de time.sleep() functie 
#(zie het hello_bliep.py script uit de eerste sessie - csd2a/session1/hello_bliep.py) samen met de duratie in de body van de forloop
#for dur in durations:
#  time.sleep(dur)
#  # and print dur
#Laad nu ook een sample in en speel deze in de body van de forloop af (zie ook het hello_bleep.py script uit de eerste sessie - csd2a/session1/hello_bleep.py)
import pygame
import time

# init  mixer module
pygame.init()

# load and play the sample
sample = pygame.mixer.Sound('../assets/plop.wav')


durations = [0.5, 1, 1.5, 0.5]


for dur in durations:
  sample.play()
  print(dur)
  time.sleep(dur)

# wait till sound is done playing before exiting
time.sleep(sample.get_length())
