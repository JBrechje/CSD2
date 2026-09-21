import pygame
import time

# init  mixer module
pygame.init()

# load and play the sample
sample = pygame.mixer.Sound('../assets/Dog2.wav')
#sample.play()


#loops the sample with while
i = 1
while i < 6:
  print(i)
  sample.play()

# wait till sound is done playing before exiting
  time.sleep(sample.get_length())

#stops loop after 5 times
  if i == 5:
    break
  i += 1