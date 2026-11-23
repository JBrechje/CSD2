#include "square.h"

// delegating constructor
Square::Square() : Oscillator(220, 0) // default frequency
{
  std::cout << "Inside Square constructor ()\n";
}

// initializer list:  used to directly initialize data members of a class.
Square::Square(float freq, float amp)
    : Oscillator(freq, amp)
{
  std::cout << "Inside Square constructor (frequency)\n";
}

Square::~Square()
{
  std::cout << "Inside Square destructor\n";
}

