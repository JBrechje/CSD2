
import pygame
import time
#import sa #simpleaudio
import random

#========================================================#
#                  greet user function                   #
#========================================================#
def greet_user():
  return "\n#========================================================#\n#             start your rythm generation!               #\n#========================================================#\n"
message = greet_user()
print("PlinCode says; ", message)

#========================================================#
#                    generate path                       #
#========================================================#
#generates a path
def generate_plinko_path(num_pulse, num_Notes):
    path = []
    count = 0


#rule 1 kick: first step must be a kick #IS NOW GENERAL!! CHANGE THIS
    for i in range(num_pulse):

        #first step
        if i == 0:
            path.append("L")
            count += 1
            continue

        remaining_steps = num_pulse - i
        remaining_notes = num_Notes - count #for every L placed kick count is plus one so remaining kicks is min 1

        #left overs need to be placed
        if remaining_notes == remaining_steps:
            step = "L"

        #if we have enough L next steps are R
        elif remaining_notes == 0:
            step = "R"

            

        #rule 2 kick: max 2 L after eachother
        #if len path is bigger then 2, 1 step previous is L, 2 steps previous is L, next step is R
        elif len(path) >= 2 and path[-1] == "L" and path[-2] == "L":
            step = "R"
        #len looks at the amount of items in a list

        #otherwise (if possible) randomly chooses L or R for next step
        else:
            step = random.choice(["L", "R"])

        #checks how many L are left over
        path.append(step)

        if step == "L":
            count += 1

    return path



num_pulse = int(input("Enter amount of pulses:\n"))
num_kickNotes = int(input("Enter amount of kicks notes:\n"))
num_snrNotes = int(input("Enter amount of snare notes:\n"))
num_HHNotes = int(input("Enter amount of hihat notes:\n"))

kick_path = generate_plinko_path(num_pulse, num_kickNotes)
print("kick path:", kick_path)
snr_path = generate_plinko_path(num_pulse, num_snrNotes)
print("snare path:", snr_path)
HH_path = generate_plinko_path(num_pulse, num_HHNotes)
print("hihat path:", HH_path)

#========================================================#
#                       play rythm                       #
#========================================================#
#make playable by samples

bpm = float(input("\nEnter bpm: "))

note_durations = kick_path #so we can later on start samples on L

quarternote_dur = 60.0 / bpm #calculate duration of a quarternote in seconds
print("\nBPM:", bpm)
print("Quarternote:", quarternote_dur)


# transform note durations to sequence of time durations
time_durations = []
for note_dur in note_durations:
    time_durations.append(quarternote_dur)#let op dus NIET * note durations, want sommige note durations zijn in mijn geval 0 en dan missen we stappen
                                            #^^^ leftover oude 0/1 systeem is nu gewoon direct van L/R systeem
print("\ntime_durations", time_durations)




#creates (general) timestamps based on the rhythm and note durations so we can later play the seperate paths from the timestamps
def create_timestamps(rhythm, note_duration):
    timestamps = []

    for i in range(len(rhythm)):
        timestamps.append(i * note_duration)

    return timestamps





# transform time durations to a sequence of timestamps
timestamp_seq = []
# use the sum of the durations to calculate the timestamp for each note
sum = 0
for time_dur in time_durations:
    timestamp_seq.append(sum)
    sum = sum + time_dur

print("timestamp_seq:", timestamp_seq)

print("\n") #for visual structure





#here are the seperate timestamp paths created and printed
kick_timestamps = create_timestamps(kick_path, quarternote_dur)
snr_timestamps = create_timestamps(snr_path, quarternote_dur)
HH_timestamps = create_timestamps(HH_path, quarternote_dur)

print("\nkick timestamps:", kick_timestamps)
print("snare timestamps:", snr_timestamps)
print("hihat timestamps:", HH_timestamps)

print("\n") #for visual structure



#########start sample choice##########
#====================================#
#         choose sample pack         #
#====================================#
#let user choose sample pack
sample_name = ["plop", "laser", "dog"] #volgorde komt overeen met de nummers in []

def sample_options(sample_name): #een functie met een lijst met namen van sample packs 
    print("option 0: " + sample_name[0]) #deze voorlegt aan gebruiker
    print("option 1: " + sample_name[1])
    print("option 2: " + sample_name[2])


    #vraag om sample
    sample_choice = int(input("Enter prefered sample:\n"))#gebruiker een keuze laat maken 

    pygame.init()
    sample_packs = [sampleKick = pygame.mixer.Sound('../assets/plop.wav'),
                    sampleSnr = pygame.mixer.Sound('../assets/Laser1.wav'),
                    sampleHH = pygame.mixer.Sound('../assets/Dog2.wav')]


    print("Sample:" + sample_name[sample_choice])

    return sample_packs[sample_choice]  #index van de keuze uit de lijst returned.
    #gebruikt index om iets uit mijn lijst sample_packs te halen

sample = sample_options (sample_name)
###########end sample choice##########



# retrieve the first time stamp
if timestamp_seq:
    ts = timestamp_seq.pop(0)
else:
    # list contains no items
    print("no timestamps --> exit")
    exit()

current_note = (0)
# store the current time
time_zero = time.time()
print("\ntime zero:", time_zero)
print("\nyour rhythm is playing...")

kick_note = 0
snr_note = 0
HH_note = 0


# iterate through time sequence and play sample
while (
    kick_note < len(kick_path)
    or snr_note < len(snr_path)
    or HH_note < len(HH_path)):
    #while current_note < len(note_durations) ......... and current_note < len(timestamp_seq):

    now = time.time() - time_zero
    # check if we passed the next timestamp,
    # if so, play sample and fetch new timestamp



    #====================================#
    #               kick                 #
    #====================================#    
    if kick_note < len(kick_timestamps):
    #and current_note < len(timestamp_seq):

        if now >= kick_timestamps[kick_note]:
            # if now >= timestamp_seq[current_note]:

            if kick_path[kick_note] == "L":
                sample.play()  #zorgt ervoor dat er alleen een noot speelt op de L (dus alle ander timestamps (R) zijn stil)
            #if note_durations[current_note] == 1:
                #sample.play()

            kick_note += 1
            #current_note += 1

              #else:
                  #no new timestamp available --> break while loop
                                
                    #break

    #====================================#
    #               snare                #
    #====================================#

    if snr_note < len(snr_timestamps):

        if now >= snr_timestamps[snr_note]:

            if snr_path[snr_note] == "L":
                sample.play()

            snr_note += 1

             #else:
                  #no new timestamp available --> break while loop
                                            
                    #break

    #====================================#
    #                hihat               #
    #====================================#

    if HH_note < len(HH_timestamps):

        if now >= HH_timestamps[HH_note]:

            if HH_path[HH_note] == "L":
                sample.play()

            HH_note += 1

            time.sleep(0.001)

             #else:
                  #no new timestamp available --> break while loop
                                            
                    #break

# wait till last sample is done playing before exit
time.sleep(time_durations[-1])
    
print("rhythm is done playing!")

#========================================================#
#                   store as midi file                   #
#========================================================#
#store as midi file
#28/9


#========================================================#
#                        TO DO                           #
#========================================================#
#adjust rules (snare & hihat)!!!!!!
#if L are left over place anyway even if its against rules

#make sample PACKS and give each instrument its own sample!!!!!!



#store as midi file^ 28/9
#code error messages 28/9


#clean up (comments and unused code)
#if time left over: add accent (or smt) based on where it lands
#                   change sample options 0, 1, 2 to 1, 2, 3
















###############################code from exercises###############################
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