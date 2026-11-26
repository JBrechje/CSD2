input melody = ["note.frequency list"];


//modulator frequency / UI parameter
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

    carrierSignal = note.frequency
    modulatorSignal = modulatorFrequency

    envelope = (1,       //atack ms
                0.25,    //decay ms
                0.5,     //sustain 0-1
                1);      //release ms

     FOR EACH sample DURING noteDuration{


            //oscillatorSample = oscillator.getSample();
            carrierSignal = carrier.getSample()/* frequency */ * carrierAmplitude;

            modulatorSignal = modulator.getSample()/* frequency */ * modulatorAmplitude;

            modOutput = carrierSignal * modulatorSignal;


            // here envelope is viewed as a signal generator, hence the getSample instead of getValue
            envelopeAmplitude = envelope.getSample();
            output = modOutput * envelopeAmplitude;


     }
} PLAY output;