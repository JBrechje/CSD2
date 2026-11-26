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

decay = decayTime;
envelope = (1,       //atack ms
            decay,   //decay ms
            0.5,     //sustain 0-1
            1);      //release ms




EACH note IN melody{

    baseFrequency = note.frequency
    baseAmplitude = amplitude


    //4 partials
    DO THIS 4 TIMES
    EACH partial IN partialRatios{

        partialFrequency = baseFrequency * partialRatio[index]; //partials frequency
        //generate oscillator for each partial
        oscillator.setFrequency(partialFrequency);


        //generate sinewave
        oscillatorSample = oscillator.getSample();


        //generate amplitude for each partial
        partialAmplitude = baseAmplitude * partialAmplitudes[index];

        // here envelope is viewed as a signal generator, hence the getSample instead of getValue
        envelopeAmplitude = envelope.getSample();

        //apply amplitude and envelope
        partialOutput = oscillatorSample * partialAmplitud * envelopeAmplitude;
        //mix partiale
        output += partialOutput;

        
     }
}PLAY output;