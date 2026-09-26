
import pygame
import time
#import sa #simpleaudio
import random

def greet_user():
  return "\n#========================================================#\n#             start your rythm generation!               #\n#========================================================#\n"
message = greet_user()
print("PlinCode says; ", message)

#========================================================#
#                    generate kick                       #
#========================================================#

#this generates a (semi) random path based on user input of pulse and kick
def generate_kick_path(num_pulse, num_kick_Notes):
    kick_path = []
    kick_count = 0


#rule 1 kick: first step must be a kick
    for i in range(num_pulse):

        #first step
        if i == 0:
            kick_path.append("L")
            kick_count += 1
            continue

        remaining_steps = num_pulse - i
        remaining_kicks = num_kick_Notes - kick_count #for every L placed kick count is plus one so remaining kicks is min 1

        #left overs need to be placed
        if remaining_kicks == remaining_steps:
            kick_step = "L"

        #if we have enough L next steps are R
        elif remaining_kicks == 0:
            kick_step = "R"

            

        #rule 2 kick: max 2 L after eachother
        #if len path is bigger then 2, 1 step previous is L, 2 steps previous is L, next step is R
        elif len(kick_path) >= 2 and kick_path[-1] == "L" and kick_path[-2] == "L":
            kick_step = "R"
        #len looks at the amount of items in a list

        #otherwise (if possible) randomly chooses L or R for next step
        else:
            kick_step = random.choice(["L", "R"])

        #checks how many L are left over
        kick_path.append(kick_step)

        if kick_step == "L":
            kick_count += 1

    return kick_path



num_pulse = int(input("Enter amount of pulses:\n"))
num_kick_Notes = int(input("Enter amount of kicks:\n"))
kick_path = generate_kick_path(num_pulse, num_kick_Notes)
print("kick:", kick_path)


#========================================================#
#                   generate snare                       #
#========================================================#
#adjust snare rules

def generate_snr_path(num_pulse, num_snr_Notes):
    snr_path = []
    snr_count = 0


    for i in range(num_pulse):

        #rule 1 snare: First step is always R/snare is never at the same time as kick
        if i == 0:
            snr_path.append("R")
            continue

        remaining_snr_steps = num_pulse - i
        remaining_snr = num_snr_Notes - snr_count

        #kick is L, so snare must be R
        if kick_path[i] == "L":
            snr_step = "R"

        #we need to place left over snares
        elif remaining_snr == remaining_snr_steps:
            snr_step = "L"

        #already have enough snares
        elif remaining_snr == 0:
            snr_step = "R"

        #otherwise randomly choose
        else:
            snr_step = random.choice(["L", "R"])

        snr_path.append(snr_step)

        if snr_step == "L":
            snr_count += 1

    return snr_path


num_snr_Notes = int(input("Enter amount of snares:\n"))
snr_path = generate_snr_path(num_pulse, num_snr_Notes)
print("snare:", snr_path)

#========================================================#
#                   generate Hihat                       #
#========================================================#
#change rules!!!
#make 16th???

#this generates a (semi) random path based on user input of pulse and snare
def generate_HH_path(num_pulse, num_HH_Notes):
    HH_path = []
    HH_count = 0


#rule 1 kick: first step must be a kick
    for i in range(num_pulse):

        #first step
        if i == 0:
            HH_path.append("L")
            HH_count += 1
            continue

        remaining_HH_steps = num_pulse - i
        remaining_HH = num_HH_Notes - HH_count #for every L placed kick count is plus one so remaining kicks is min 1

        
        #left overs need to be placed
        if remaining_HH == remaining_HH_steps:
            HH_step = "L"

        #if we have enough L next steps are R
        elif remaining_HH == 0:
            HH_step = "R"

            

        #rule 2 kick: max 2 L after eachother
        #if len path is bigger then 2, 1 step previous is L, 2 steps previous is L, next step is R
        elif len(HH_path) >= 2 and HH_path[-1] == "L" and HH_path[-2] == "L":
            HH_step = "R"
        #len looks at the amount of items in a list

        #otherwise (if possible) randomly chooses L or R for next step
        else:
            HH_step = random.choice(["L", "R"])

        #checks how many L are left over
        HH_path.append(HH_step)

        if HH_step == "L":
            HH_count += 1

    return HH_path


num_HH_Notes = int(input("Enter amount of Hihats:\n"))
HH_path = generate_HH_path(num_pulse, num_HH_Notes)
print("Hihat:", HH_path)

print("your complete path:", "\nkick: ", kick_path, "\nsnare:", snr_path, "\nhihat:", HH_path)

#========================================================#
#                    L/R to 1/0 rhythm                   #
#========================================================#
#readable rhythm



#========================================================#
#                   choose sample pack                   #
#========================================================#
#let user choose sample pack



#========================================================#
#                       play rythm                       #
#========================================================#
#make playable by samples


#========================================================#
#                   store as midi file                   #
#========================================================#
#store as midi file



#========================================================#
#                        TO DO                           #
#========================================================#
#adjust rules (snare & hihat)
#make playable by samples^
#let user choose sample pack^
#store as midi file^
#user input bpm

#clean up (comments and unused code)
#if time left over: add accent (or smt) based on where it lands
































































"""

def generate_path(num_pulse, num_kickNotes):
    path = []
    kick = 0
    # hier komt de Plinko-logica
"""
"""
    return path

path = generate_path(num_pulse, num_kickNotes)
print(path)
"""



"""
######################generates l r path to 1 0
def path_to_rhythm(path):
    rhythm = []
    for step in path:
      if step == "L":
        rhythm.append(1)
      else:
        rhythm.append(0)

    return rhythm

path = ["L", "R", "R", "L", "R", "L", "R", "R"] 
kick = path_to_rhythm(path)

print(kick)

"""
##############################################################


"""
num_notes = input("Enter num notes\n")
note_durations = list()

for i in range(int(num_notes)):
    note_durations.append(float(input("Enter note duration\n")))

print("note_durations:", note_durations)

#vraag bpm op & bereken quarternote
bpm = float(input("Enter BPM\n"))
quarternote_dur = 60.0 / bpm
print("bpm:", bpm, "quarternote_dur", quarternote_dur)


"""
"""

#sample options
def sample_options(optionName):
  print("option: " + optionName)

sample_options("1 dog")
sample_options("2 plop")
sample_options("3 drum")

#vraag om sample
sample_choice = (input("Enter prefered sample\n"))
print("sample: ", sample_choice)

"""
"""


#note durations wordt time durations
time_durations = []
for note_dur in note_durations:
    time_durations.append(quarternote_dur * note_dur)

print("time_durations", time_durations)

"""
"""

#time duration wordt time stamp
timestamp_seq = []
#telt de duraties op om de timestamp uit te rekenen
sum = 0
for time_dur in time_durations:
    timestamp_seq.append(sum)
    sum = sum + time_dur

print("timestamp_seq:", timestamp_seq)

"""
"""
#laadt sample
pygame.init()
sample = pygame.mixer.Sound('../assets/plop.wav')


#eerste time stamp
if timestamp_seq:
    ts = timestamp_seq.pop(0)
else:
    #waarneer een lijst geen items heeft
    print("no timestamps --> exit")
    exit()

#slaat current time op
time_zero = time.time()
print("time zero:", time_zero)

#iterate through time sequence and play sample
while True:
    now = time.time() - time_zero
    #is de vorige time stamp true?
    #ja? volgende time stamp
    if(now >= ts):
        sample.play()
        if timestamp_seq:
            ts = timestamp_seq.pop(0)
        else:
            #no new timestamp available --> break while loop
            break

    time.sleep(0.001)

#wacht tot het eind vd laatste sample daarna pas exiten
time.sleep(time_durations[-1])


"""

"""
choose_sample = input("Enter preferred sample:\n")
pygame.init()
samples = [ pygame.mixer.Sound("../assets/plop.wav"),
            pygame.mixer.Sound("../assets/Laser1.wav"),
            pygame.mixer.Sound("../assets/Dog2.wav")]

sample = samples
"""


"""
#tijd
#note_duration omzetten naar tijd (sec)
time_durations = []
for note_dur in note_durations:
    time_durations.append(quarternote_dur * note_dur)

print("time_durations", time_durations)





# ___ play rhythm ___
# load a sample
sample_plop = sa.WaveObject.from_wave_file("../assets/Plop.wav")

# retrieve current time to store as t = 0
time_zero = time.time()
# allow to calcultate time duration sum according to time durations
time_seq_sum = 0
# play rhythm
for time_dur in time_durations:
    # calculate time deviation
    time_now = time.time() - time_zero
    time_deviation = time_now - time_seq_sum
    print("time_deviation:", time_deviation)
    # play sample and pause according to time duration
    sample_plop.play()
    time.sleep(time_dur)
    # update time sum
    time_seq_sum += time_dur
"""

"""
# ___ play rhythm ___
# init  mixer module and load sample
pygame.init()
sample = pygame.mixer.Sound('../assets/plop.wav')

# play sequence
for time_dur in time_durations:
    # play sample and pause according to time duration
    sample.play()
    time.sleep(time_dur)
"""






"""
# init  mixer module and load samples
pygame.init()
sampleHigh = pygame.mixer.Sound('../assets/plop.wav')
sampleMid = pygame.mixer.Sound('../assets/Laser1.wav')
sampleLow = pygame.mixer.Sound('../assets/Dog2.wav')

# play high sample
sampleHighPlay = sampleHigh.play()
# wait till sample is done playing
time.sleep(sampleHigh.get_length())

# play mid sample
sampleMidPlay = sampleMid.play()
# wait till sample is done playing
time.sleep(sampleMid.get_length())

# play low sample
sampleLowPlay = sampleLow.play()
# wait till sample is done playing
time.sleep(sampleLow.get_length())
"""