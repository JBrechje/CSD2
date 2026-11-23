#include "sine.h"

// delegating constructor
Sine::Sine() : Oscillator(220, 0) // default frequency
{
  std::cout << "Inside Sine constructor ()\n";
}

// initializer list:  used to directly initialize data members of a class.
Sine::Sine(float freq, float amp)
    : Oscillator(freq, amp)
{
  std::cout << "Inside Sine constructor (frequency)\n";
}

Sine::~Sine()
{
  std::cout << "Inside Sine destructor\n";
}

