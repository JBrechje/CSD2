#include <iostream>
#include "oscillator.h"

// 3 type access specifiers:
// public, protected, private
class Square : public Oscillator
{
  public:
  Square();
  Square(float freq, float amp);
  ~Square();
};
