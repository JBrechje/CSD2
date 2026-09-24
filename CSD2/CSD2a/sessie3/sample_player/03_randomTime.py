"""
An example project in which three wav files are played one after the other with a
break in between of a random duration.
Used durations are: 0.125, 0.25 and 0.5 seconds

------ EXERCISES ------
- Alter the code:
  Add a noteDurations list, with the numbers 0.25, 0.5, 1.0. These values stand
  for a sixteenth, eighth and quarter note.
  Add a bpm variable to the project and calculate the corresponding timeIntervals
  accordingly. Add these values to the timeIntervals list, instead of its
  current values.

- Alter the code:
  Write a function around the playback forloop, which takes two arguments:
  - a list with samples
  - a list with timeIntervals
  Use this function.
"""

import pygame
import time
import random


# init  mixer module and load audio files into a list
pygame.init()
samples = [ pygame.mixer.Sound("../assets/plop.wav"),
            pygame.mixer.Sound("../assets/Laser1.wav"),
            pygame.mixer.Sound("../assets/Dog2.wav")]

#note duration list
noteDurations = [0.25, 0.5, 1]
bpm = 120

timeIntervals = []

#calculates a quarternote based on the bpm
quarterNote = 60.0 / bpm

print("quarternote:", quarterNote)


# create a list to hold the timeIntervals 0.25, 0.5, 1.0
timeIntervals = [0.25, 0.5, 1]

for noteDuration in noteDurations:
  #calculate time duration and add to the list
  timeIntervals.append(quarterNote * noteDuration)

# display timeIntervals
print("Selection of time intervals: ", timeIntervals )

def samplePlayer (samples, intervals):
# play samples and wait in between (random duration)
  for sample in samples:
    print(sample)
    sample.play()

    # get a random value to be used as sample index
    randomIndex = random.randint(0, 2)

    # dislay the selected timeInterval
    #print("waiting: " + str(timeIntervals[randomIndex]) + " seconds.")

    timeInterval = random.choice(intervals)
    print("waiting: " + str(timeInterval) + " seconds.")
    time.sleep(timeInterval)

    # wait some time
    #time.sleep(timeIntervals[randomIndex])

    #play loop 4 times
    for i in range(4):
      samplePlayer(samples, timeIntervals)
