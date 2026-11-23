#include "oscillator.h"
#include "saw.h"
#include "square.h"
#include "sine.h"

int main()
{
  std::cout << "\nin main\n";

  Oscillator osc(220, 0.5);
  Saw saw(220, 0.5);
  Square square(220, 0.5);
  Sine sine(220, 0.5);

////osc
  std::cout << "Frequency of the Oscillator object osc is: "
    << osc.getFreq() << "\n";

  osc.setFreq(440);
  std::cout << "Frequency of the Oscillator object osc is: "
    << osc.getFreq() << "\n";

////saw
  std::cout << "Frequency of the Saw object osc is: "
    << saw.getFreq() << "\n";

  saw.setFreq(440);
  std::cout << "Frequency of the Saw object osc is: "
    << saw.getFreq() << "\n";

////square
  std::cout << "Frequency of the Square object osc is: "
    << square.getFreq() << "\n";

  square.setFreq(440);
  std::cout << "Frequency of the Square object osc is: "
    << square.getFreq() << "\n";

////sine
  std::cout << "Frequency of the Sine object osc is: "
    << sine.getFreq() << "\n";

  sine.setFreq(440);
  std::cout << "Frequency of the Sine object osc is: "
    << sine.getFreq() << "\n";
    

  // end program
  return 0;
}
