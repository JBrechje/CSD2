#include <iostream>

class ZipCode{
public:
  // default constructor
  ZipCode();
  // overloaded constructor
  ZipCode(int code);

  // fields
  int zip;
};

ZipCode::ZipCode() {
  std::cout << "ZipCode - default constructor\n";
  // NOTE: duplicate code alarm!!
  // constructor delegation is a better strategy!

  zip = 1234;
}

ZipCode::ZipCode(int code) {
  std::cout << "ZipCode - constructor with float diam parameter\n";

  zip = code;
}

// TODO - add woofer
class HouseNumber{
  public:
  // default construtor
  HouseNumber();
  // overloaded constructor
  HouseNumber(int num);

  // fields
  int house;
};
  
HouseNumber::HouseNumber(){
std::cout<< "HouseNumber - default constructor\n";

house = 42;
}

HouseNumber::HouseNumber(int num) {
  std::cout << "HouseNumber - constructor with float diam parameter\n";

  house = num;
}


class Adress{
public:
  Adress();
  ZipCode aZipCode;
  HouseNumber aHouseNumber;
};

Adress::Adress() {
  std::cout << "Adress - constructor\n";
  aZipCode.zip = 1234;
  std::cout << "Your zipcode is: " // 1234
    << aZipCode.zip << "\n";

  aHouseNumber.house = 42;
  std::cout << "your housenumber is: " // 42
    << aHouseNumber.house << "\n";
}

int main() {
  Adress aAdress;
};
