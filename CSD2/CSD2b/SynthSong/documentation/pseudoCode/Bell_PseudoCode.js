input melody = ["note.frequency list"];


//decayTime / ui parameter
ASK decayTime(): "how long do you want the decayTime?"
    
VALIDATE decayTime()

    if decayTime == valid{
        continue
    }
    else {
        "try again"
        RETURN TO (ASK decayTime)

    }


// INITIALIZE PARTIALS
partialRatios = [1.0, 2.0, 3.5, 4.2, 5.4];

partialAmplitudes = [1.0, 0.5, 0.3, 0.2, 0.1];




EACH note IN melody{

    baseFrequency = note.frequency
    baseAmplitude = amplitude


    //4 partials
    DO THIS 4 TIMES
    EACH partial IN partialRatios{


        partialFrequency = baseFrequency * partial.ratio; //partials frequency
        
        //create oscillator for each partial
        oscillator.setFrequency(partialFrequency);

        //amplitude for each partial
        partialAmplitude = partial.amplitude;


        //generate sinewave
        oscillatorSample = oscillator.getSample();

        // here envelope is viewed as a signal generator, hence the getSample instead of getValue
        amplitude = envelope.getSample();


        //apply amplitude and envelope
        partialOutput = oscillatorSample * partialAmplitude;

        //mix partiale
        noteOutput += partialOutput;



        partial = partialFreqcuency + partialAmplitude

        
     }
      // Send note output to audio output
    PLAY noteOutput;
}







/////////////////////UI////////////////////////////

/*
ASK parameters "Change parameters?"{

    if userSelects(yes){
        RETURN TO (ASK decayTime)
    } 
    else{
        DISPLAY "Save?"
    }
}END IF


ASK filename "enter filename"{  
    VALIDATE (filename)
        if filename == valid{
        continue
    }
    else {
        "invalid name"
        RETURN TO (ASK filename)
    } SAVE "file saved as ...."
} END*/