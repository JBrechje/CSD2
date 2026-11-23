#include <iostream>
#include "oscillator.h"

// 3 type access specifiers:
// public, protected, private
class Sine : public Oscillator
{
  public:
  Sine();
  Sine(float freq, float amp);
  ~Sine();
};
