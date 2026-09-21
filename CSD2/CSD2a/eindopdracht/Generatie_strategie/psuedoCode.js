//user inputs:
//pulse/time signature
//amount of notes
//bpm



let pulse = [/*user input between [] & []*/];
let note = [/*user input between [1] & [(pulse)]*/]; //example: if pulse is 7, notes is 1 to 7

/////////////kick/////////////
apply kick rules {
    step 1 is always L
}

(amount of steps == (pulse));
(amount of L is (notes));
(amount of R steps is (pulse)-(notes)); 

    flip a coin (50% L/50% R);
    if (L){
        write note
    } 
    if (R){
        write rest
    } 

    does this violate a rule?
        YES -> dont allow this direction
        NO  -> allow it
    make kick list [];

/////////////snare////////////
apply snare rules {
    look up list kick
    never at the same time as kick
}
      

(amount of steps == (pulse));
(amount of L steps is (notes)); //amount of snare notes/L steps???? 
(amount of R steps is (pulse)-(notes)); 

    flip a coin (50% L/50% R);
    if (L){
        write note
    } 
    if (R){
        write rest
    } 

    does this violate a rule?
        YES -> dont allow this direction
        NO  -> allow it
    make snare list [];

//////////////HH/////////////////
apply HH rules {
    look up list kick
    look up list snare
    (HHnotes = notes * 2)
}

(amount of steps == (pulse));
(amount of L is (notes));
(amount of R steps is (pulse)-(notes)); 

    flip a coin (50% L/50% R);
    if (L){
        write note
    } 
    if (R){
        write rest
    } 

    does this violate a rule?
        YES -> dont allow this direction
        NO  -> allow it
    make HH list [];



repeat 4 times (4 bars) 
add together



//save as midi
save as midi file 
[yes][no]
if (yes){
    save as midi file
}
else {
    ask to run again [A]
    or
    go back to the begin [B]
        if (A) {
            run again
        }
        else {
            back to begin
        }
}



