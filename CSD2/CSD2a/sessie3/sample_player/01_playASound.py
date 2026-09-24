"""
An example project in which three wav files are used.

------ EXERCISES ------

- Answer the following question before running the code:
  Do you expect to hear the samples played simultaneously or one after the other?
  Why?
  tegelijkertijd omdat niks aangeeft dat er de een sample zou moeten wachten op iets met afspelen.

- Alter the code:
  Play the sounds one after the other and then simultaneously.


- Alter the code:
  Ask the user to choice which one of the three samples should be played and
  only play the chosen sample.

- Give yourself a couple of assignments, like playing one of the samples ten
  times before the others are played, playing all samples a given number
  of times or playing the samples one after the other with 1 second between
  them.

"""

# simpleaudio is imported as sa -> shorter name
import pygame
import time
import simpleaudio as sa

# init  mixer module and load samples
pygame.init()
samples = [pygame.mixer.Sound('../assets/plop.wav'),
          pygame.mixer.Sound('../assets/Laser1.wav'),
          pygame.mixer.Sound('../assets/Dog2.wav')]


# play samples, wait 1 second in between
for sample in samples:
  print(sample) # display the sample object
  sample.play() # play sample
  time.sleep(0.5) # wait 0.5 second

'''
# play high sample
sampleHighPlay = sampleHigh.play()
# wait till sample is done playing
time.sleep(sampleHigh.get_length())

# play mid sample
sampleMidPlay = sampleMid.play()
# wait till sample is done playing
time.sleep(sampleMid.get_length())

# play low sample
sampleLowPlay = sampleLow.play(2, 5)
# wait till sample is done playing
time.sleep(sampleLow.get_length())
'''