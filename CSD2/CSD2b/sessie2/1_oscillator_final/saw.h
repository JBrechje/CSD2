#include <iostream>
#include "oscillator.h"

// 3 type access specifiers:
// public, protected, private
class Saw : public Oscillator
{
public:
  Saw();
  Saw(float freq, float amp);
  ~Saw();
};
