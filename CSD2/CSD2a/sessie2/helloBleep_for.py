import pygame
import time

# init  mixer module
pygame.init()

# load and play the sample
sample = pygame.mixer.Sound('../assets/Dog2.wav')
#sample.play()

#loops the sample with for
numbers = ["10", "20", "30"]
for x in numbers:
  print("for", x)
  sample.play()

  # wait till sound is done playing before exiting
  time.sleep(sample.get_length())