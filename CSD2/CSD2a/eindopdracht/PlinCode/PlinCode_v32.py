import pygame
import time
from midiutil import MIDIFile
#import simpleaudio
import random

#====================== greet user function ======================#
def greet_user():
  return "\n#========================================================#\n#             start your rythm generation!               #\n#========================================================#\n"
message = greet_user()
print("PlinCode says; ", message)

#====================== generate path ======================#
correctPulse = False
correctInput = False
num_pulse = 11 #default value

def generate_plinko_path(num_pulse, num_Notes, blocked_path = None):
    path = []
    count = 0

    for i in range(num_pulse):

        #if there step is 0 all steps are silent
        if num_Notes == 0:
            step = "R"

        #rule 4: snare may never be on 1
        elif blocked_path is not None and i == 0:
            step = "R"

        #rule 1 kick: first step must be a kick
        elif blocked_path is None and i == 0:
            step = "L"

        else: #for every L placed instrument note count is +1 one so remaining notes is -1
            remaining_steps = num_pulse - i
            remaining_notes = num_Notes - count

            #left overs need to be placed
            if remaining_notes == remaining_steps:
                step = "L"

            #if all L are placed next steps are R
            elif remaining_notes == 0:
                step = "R"

            #rule 3: snare is never at the same time as the kick
            elif blocked_path is not None and blocked_path[i] == "L":
                step = "R"

            #rule 2 kick: max 2 L after eachother
            elif len(path) >= 2 and path[-1] == "L" and path[-2] == "L":
                step = "R"

            else: #otherwise (if possible) randomly chooses L or R for next step
                step = random.choice(["L", "R"])

        path.append(step)

        if step == "L":
            count += 1

    return path


while (not correctPulse):
    user_input = input("Enter amount of pulses:\n")

    if user_input == "":
        # empty string --> use default
        num_pulse = 11
        correctPulse = True
    else:
        try:
            num_pulse = int(user_input)

            if 3 <= num_pulse <= 25:
                correctPulse = True
            else:
                print("pulse must be between 3 and 25")
        except ValueError:
            print("Incorrect input, please enter a whole number between 3 and 25 (or leave empty for default).")


while (not correctInput):
    user_kickNotes = input("\nenter amount of kick notes: ")
    user_snrNotes = input("Enter amount of snare notes: ")
    user_HHNotes = input("Enter amount of hihat notes: ")
    #check if we 'received' an empty string
    if not user_kickNotes and not user_snrNotes and not user_HHNotes:
        num_kickNotes = 3
        num_snrNotes = 3
        num_HHNotes = 3
        #empty string --> use default
        correctInput = True
    else:
        try:
            num_kickNotes = int(user_kickNotes)
            num_snrNotes = int(user_snrNotes)
            num_HHNotes = int(user_HHNotes)

            #check that every amount is between 1 and the number of pulses
            if (
                0 <= num_kickNotes <= num_pulse
                and 0 <= num_snrNotes <= num_pulse
                and 0 <= num_HHNotes <= num_pulse
            ):
                correctInput = True
            else:
                print(
                    "all note amounts must be whole numbers between 0 and the amount of pulses (or leave empty for default)."
                    ) 
        except ValueError:
            print(
                "Incorrect input, please enter whole numbers between 0 and the amount of pulses (or leave empty for default)"
            )
            
print("\namount of pulses:", num_pulse)
print("Kick notes:", num_kickNotes)
print("Snare notes:", num_snrNotes)
print("Hihat notes:", num_HHNotes)

kick_path = generate_plinko_path(num_pulse, num_kickNotes)
snr_path = generate_plinko_path(num_pulse, num_snrNotes, blocked_path = kick_path) 
#blocked path so its not at the same time as the kick
HH_path = generate_plinko_path(num_pulse, num_HHNotes)

print("kick path:", kick_path)
print("snare path:", snr_path)
print("hihat path:", HH_path)

#====================== choose bpm ======================#
correctInput = False
bpm = 120 #default bpm

while (not correctInput):
    user_bpm = input("\nenter BPM: ")
    #check if we 'received' an empty string
    if not user_bpm:
        #empty string --> use default
        correctInput = True
    else:
        try:
            bpm = float(user_bpm)

            if bpm >= 100 and bpm <= 300:
                correctInput = True
            else:
                print("BPM must be greater than 100 and smaller than 300 (or leave empty for default).")

        except:
            print("Incorrect input, please enter a BPM (or leave empty for default)")
            
print("BPM is: ", bpm)

#====================== create events ======================#
def create_events(rhythm, instrument_name, bpm, sample):
    events = []
    quarternote_dur = 60.0 / bpm #calculate in seconds
    print("\nQuarternote:", quarternote_dur)

    for i, step in enumerate(rhythm):
        if step == "L":
            events.append({
                'timestamp': i * quarternote_dur,
                'sample_name': instrument_name,
                "sample": sample,
                "velocity": 100,
                "duration_msec": 1000
            })

        #timestamp += time_dur_seq[i]
    return events

    return events


#print("Kick events:", kick_events)
#print("Snare events:", snr_events)
#print("Hihat events:", HH_events)

print("\n") #for visual structure

#========= transform ===============#
#transform durations (quarternote) into time (sec)
note_dur_seq = [1 for step in kick_path] #quarternotes

def to_time_dur(src_seq, bpm):
    dst_seq = []
    dur_multiplyer = 60.0 / bpm


    #iterate through the source sequence, add duration values to destiation seq
    for note_dur in src_seq:
        dst_seq.append(note_dur * dur_multiplyer)

    return dst_seq

#function to transform a sequence with durations in time (sec.) into
#a sequence with timestamps
def to_timestamp_seq(src_seq):
    dst_seq = []
    timestamp = 0
    #iterate through the source sequence, sum durations and store these as
    #timestamp in the destination Sequence
    for time_dur in src_seq:
        dst_seq.append(timestamp)
        timestamp += time_dur

    return dst_seq


#call the to_time function and store the restulting sequence
time_dur_seq = to_time_dur(note_dur_seq, bpm)
# transform the list with note duration into a list with timestamps
timestamp_seq = to_timestamp_seq(time_dur_seq)

print("Sequence with quarter note values:", note_dur_seq)
print("Sequence with duration values in seconds:", time_dur_seq)
print("Sequence with timestamp values in seconds:", timestamp_seq)

#========= choose sample pack =========#
pygame.init()
sample_question = "Choose your samplepack: "
sample_options = ["plop", "regular drumkit", "extra drumkit"]
sample_packs = [ [ 
                        pygame.mixer.Sound('assets/plop.wav'), 
                        pygame.mixer.Sound('assets/Dog2.wav'), 
                        pygame.mixer.Sound('assets/Laser1.wav')], 
                        [ 
                        pygame.mixer.Sound('assets/kick.wav'), 
                        pygame.mixer.Sound('assets/snare.wav'), 
                        pygame.mixer.Sound('assets/hihat.wav')], 
                    [ 
                        pygame.mixer.Sound('assets/kick2.wav'), 
                        pygame.mixer.Sound('assets/snare2.wav'), 
                        pygame.mixer.Sound('assets/hihat2.mp3')] 
                        ] 

def retrieve_user_input(question, options):
    # be sure the question is a string
    if(not str(question)):
        raise TypeError(
            "retrieve_user_option function expects first parameter to be a string")
    # present user with options and ask for selection
    print(question)
    for i, option in enumerate(options):
        print(i + 1, ":", option)
    print("leave empty for default option 1")
    return input()


def validate_int_in_inclusive_range(value, range_low, range_high):
    try:
        int_value = int(value)
        if (int_value >= range_low and int_value <= range_high):
            # int and in range
            return True
    except:
        # no valid int
        return False
    # not in range
    return False

def retrieve_user_option(question, options):
    #default option +1 for readability for user
    selected_option = 1
    correctInput = False

    while (not correctInput):
        user_input = retrieve_user_input(question, options)
        # validate user input
        if(validate_int_in_inclusive_range(user_input, 1, len(options))):
            # user input is in given range
            selected_option = int(user_input)
            correctInput = True
        # if answer is empty --> use default value
        elif(not user_input):
            correctInput = True
        # else incorrect input -->  retry
        else:
            print("Incorrect input, please enter a valid value of 1, 2 or 3 (or leave empty for default).\n" +
                "Please try again.\n\n")

    #user chooses 1, 2 or 3
    #python uses 0, 1 or 2
    selected_option -= 1

    #get the selected pack
    selected_pack = sample_packs[selected_option]

    #get the three samples
    sampleKick = selected_pack[0]
    sampleSnr = selected_pack[1]
    sampleHH = selected_pack[2]

    print("Selected drumkit:", options[selected_option])

    return sampleKick, sampleSnr, sampleHH

sampleKick, sampleSnr, sampleHH = retrieve_user_option(
    sample_question,
    sample_options)


kick_events = create_events(kick_path, "kick", bpm, sampleKick)
snr_events = create_events(snr_path, "snare", bpm, sampleSnr)
HH_events = create_events(HH_path, "hihat", bpm, sampleHH)


def get_timestamp(event):
    return event["timestamp"]


#combine & sort all events
all_events = kick_events + snr_events + HH_events

print("--- event List ---")
for event in all_events:
    print(event)

all_events.sort(key = get_timestamp)
print("events sorted by timestamps:", all_events)

#====================== play rythmm 4 times ======================#
def handle_note_event(event):
    """handles note events by playing the referenced sample"""
    print("Handling note event, sample name:", event["sample_name"])
    sample = event["sample"]
    sample.set_volume(event["velocity"] / 127.0)
    sample.play()
    
    
for repetition in range(4):
    time_zero = time.time()
    print("\ntime zero:", time_zero)
    print("\nyour rhythm is playing...")
    event_index = 0

    while event_index < len(all_events):

        now = time.time() - time_zero

        event_time = all_events[event_index]["timestamp"]
        if now >= event_time:
            handle_note_event(all_events[event_index])
            event_index += 1
        else:
            time.sleep(0.01) #so the samples dont overlapp while looping

print("rhythm is done playing!")

#====================== store as midi file ======================#
def save_rhythm_as_midi(kick_path, snr_path, HH_path, bpm, filename):
# create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, bpm)
        
    # add some notes
    channel = 9  #midi channel 10 = drums
    volume = 80

    #midi pitches
    kick_pitch = 35
    snare_pitch = 38
    hihat_pitch = 42

    duration = 1 # 1 beat long


    instruments = {
        "kick": (kick_path, kick_pitch),
        "snare": (snr_path, snare_pitch),
        "hihat": (HH_path, hihat_pitch)
    }


    for path, pitch in instruments.values():
        for i, step in enumerate(path):
            if step == "L":
                mf.addNote(track, channel, pitch, i, duration, volume)                          
        #                                         i = time

    # write it to disk
    with open(filename, "wb") as outf:
        mf.writeFile(outf)
    print("MIDI saved as:", filename)

    #ui for midi file name and saving
save_midi = input(
    "\nWould you like to save this rhythm as a MIDI file? (y/n): "
)
while save_midi.lower() not in ["y", "n"]:
    print("Incorrect input - please enter y or n.")
    save_midi = input(
        "Would you like to save this rhythm as a MIDI file? (y/n): "
    )

if save_midi.lower() == "y":

    filename = input(
        "Enter a filename (without .mid): "
    )

    if not filename:
        filename = "plincode_rhythm"

    filename = filename + ".mid"

    save_rhythm_as_midi(
        kick_path,
        snr_path,
        HH_path,
        bpm,
        filename
    )
else:
    print("MIDI file was not saved.")