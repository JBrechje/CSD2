input melody = ["note.frequency list"];


//decayTime / ui parameter
ASK modulatorFrequency(): "how long do you want the decayTime?"
    
VALIDATE modulatorFrequency()

    if modulatorFrequency == valid{
        continue
    }
    else {
        "try again"
        RETURN TO (ASK modulatorFrequency)

    }


FOR EACH note IN melody{

    carrierFrequency() = note.frequency

     FOR EACH sample DURING noteDuration{


            //ciskas
            oscillatorSample = oscillator.getSample();
            // here envelope is viewed as a signal generator, hence the getSample instead of getValue
            amplitude = envelope.getSample();
            output = oscillatorSample * amplitude;


            ////////??/////
            carrierSignal = carrier.getSample()/* frequency */ * carrierAmplitude;

            modulatorSignal = modulator.getSample()/* frequency */ * modulatorAmplitude;

            output = carrierSignal * modulatorSignal;


            /*
            carrierSignal = carrierFrequency * carrierAmplitude
            modulatorSignal =  modulatorFrequency * modulatorAmplitude

            output = carrierSignal * modulatorSignal*/

     }
} PLAY noteOutput;






////////////////UI///////////////////

/*
ASK parameters "Change parameters?"{

    if userSelects(yes){
        RETURN TO (ASK modulatorFrequency)
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




