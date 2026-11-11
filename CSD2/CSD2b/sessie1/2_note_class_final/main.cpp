#include <iostream>

/*
 * class - implementation steps
 * 1. define the class
 * 2. define the constructor
 * 3. implement the constructor
 * 4. add fields / methods (and define the methods)
  
 
 Lees het Note voorbeeld in de map 
 _session1/2_note_class_final. Wat is/zijn de 
 constructor, methods en fields van Note?
 * constructor is een onderdeel van een class en heeft 
  dezelfde naam als de class.
 * method is een function & een onderdeel van een class.
 * field is een onderdeel van een class.
 */



class Note {
public:
  // default constructor
  Note(); // same name as class name

   // tweede constructor
  Note(int midiNoteValue, int velocity);

  // methods (a method is a function & a member of a class)
  // NOTE: for the sake of the example,
  //  play should probably not be part of the Note class
  // void --> no return
  void play();
  // int --> returns an integer
  int getVelocity();
  // fields (a field is a member of a class)
  int midiNoteValue;
  int velocity;
};


Note::Note() {
  std::cout << "Note - constructor\n";
  this->midiNoteValue = 0;
  this->velocity = 0;
}

Note::Note(int midiNoteValue, int velocity) {
  std::cout << "Note - constructor\n";
  this->midiNoteValue = midiNoteValue;
  this->velocity = velocity;
}

void Note::play() {
  std::cout << "PLAYING NOTE: " << midiNoteValue
    << " at velocity: " << velocity << std::endl;
}

int Note::getVelocity() {
  return velocity;
}

int main() {
  Note aNote;
  Note AnotherNote(3, 1);

  std::cout << "\nObject aNote - midiNoteValue: " << aNote.midiNoteValue << std::endl; //verwacht return 0
  std::cout << "\nObject aNote - velocity: " << aNote.velocity << std::endl; //verwacht return 0
  std::cout << "\nObject anotherNote - midiNoteValue: " << AnotherNote.midiNoteValue << std::endl; //verwacht return 3
  std::cout << "\nObject anotherNote - velocity: " << AnotherNote.velocity << std::endl; //verwacht return 1


  aNote.midiNoteValue = 60;
  aNote.velocity = 127;
  aNote.play();
}
