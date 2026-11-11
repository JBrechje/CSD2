#include <iostream>

/*
 * class - implementation steps
 * 1. define the class   (done)
 * 2. define the constructor (done)
 * 3. implement the constructor (done)
 * 4. add fields / methods (and define the methods)
 */

/*class Note {
public:
  Note() {
    std::cout << "\nNote constructor.\n";
  }

  int getMidiValue() {
    return midiValue;
  }

  int midiValue = 120;
}; */



class Note {
  // default constructor
public:
  // constructor
   Note(int midiNote);

    //default midi note value 60
    int midiNote;
    int shiftOctaveUp();
};

//Class::Constructor
Note::Note(int midiNote)
{
  // body of constructor  
  // implimentatie
  std::cout << "\nNote::Note() - inside the constructor of the Note class" << std::endl;
  std::cout << "\nparameter midiNoteValue" << midiNote << std::endl;
  //this pointer --> to indicate class field
  this->midiNote = midiNote;
}

int Note::shiftOctaveUp()
{
  return midiNote + 12;
}

int main() {
  Note note(64);
  Note anotherNote(40);
  std::cout << "\nObject note - midiNote: " << note.midiNote << std::endl; //verwacht return 64
  std::cout << "\nObject note - shiftOctaveUp returns: " << note.shiftOctaveUp() << std::endl; //verwacht een octaaf hoger 76
  std::cout << "\nObject anotherNote - midiNote: " << anotherNote.midiNote << std::endl; //verwacht return 40
  std::cout << "\nObject anotherNote - shiftOctaveUp returns: " << anotherNote.shiftOctaveUp() << std::endl; //verwacht een octaaf hoger 52
  //std::cout << "\nRetrieving the note frequency, freq is: " << note1.midiValue;
  std::cout << "\nReached the end of the application.\n"; //einde
}
