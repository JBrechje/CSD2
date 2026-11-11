#include <iostream>

class Tweeter{
public:
  // default constructor
  Tweeter();
  // overloaded constructor
  Tweeter(float diam);

  // fields
  float diameter;
  float conePosition;
};

Tweeter::Tweeter() {
  std::cout << "Tweeter - default constructor\n";
  // NOTE: duplicate code alarm!!
  // constructor delegation is a better strategy!

  // in cm
  diameter = 2.5f;
  // number with an f --> indicate it is a float
  conePosition = 0.0f;
}

Tweeter::Tweeter(float diam) {
  std::cout << "Tweeter - constructor with float diam parameter\n";
  // in cm
  diameter = diam;
  // number with an f --> indicate it is a float
  conePosition = 0.0f;
}

// TODO - add woofer
class Woofer{
  public:
  // default construtor
  Woofer();
  // overloaded constructor
  Woofer(float diam);

  // fields
  float diameter;
  float conePosition;
};
  
Woofer::Woofer(){
std::cout<< "Woofer - default constructor\n";
// in cm
diameter = 4.8f;
// number with an f --> indicate it is a float
conePosition = 1.0f;
}

Woofer::Woofer(float diam) {
  std::cout << "Woofer - constructor with float diam parameter\n";
  // in cm
  diameter = diam;
  // number with an f --> indicate it is a float
  conePosition = 2.0f;
}


class Speaker{
public:
  Speaker();
  Tweeter aTweeter;
  Woofer aWoofer;
};

Speaker::Speaker() {
  std::cout << "Speaker - constructor\n";
  aTweeter.diameter = 2.4;
  std::cout << "The diameter of the tweeter is: " //2.4
    << aTweeter.diameter << "\n";

  aWoofer.diameter = 2.4;
  std::cout << "The diameter of the Woofer is: "  //4.8
    << aWoofer.diameter << "\n";
}

int main() {
  Speaker aSpeaker;
};
