#include "saw.h"
#include "oscillator.h"

// delegating constructor
Saw::Saw() : Oscillator(220, 0) // default frequency
{
  std::cout << "Inside Saw constructor ()\n";
}

// initializer list:  used to directly initialize data members of a class.
Saw::Saw(float freq, float amp) 
    : Oscillator(freq, amp)
{
  std::cout << "Inside Saw constructor (frequency)\n";
}

Saw::~Saw()
{
  std::cout << "Inside Saw destructor\n";
}