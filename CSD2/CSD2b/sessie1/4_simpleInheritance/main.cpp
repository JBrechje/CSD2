#include "dog.h"
#include "cat.h"

/*
[READ] In de cpp file staat: // overloaded constructor. Wat betekent dit?
 * Als je dezelfde naam voor verschillende constructors gebruikt
  bv; Postcode() & Postcode(int HuisNummer)


[READ] In de cpp file staat: // constructor delegation is a better strategy!, wat betekent dit?
 * dat je code in een class meerdere keren kan gebruiken in verschillende construtors (zonder ze opnieuw te typen)
  bv; in de class "Pet" kan je de constructor Pet(Dog) en Pet(Cat) aanroepen

[WRITE] Voeg een method toe aan de base class, bijv. drink. (done)
[WRITE] Voeg een extra derived class toe die erft van de base class Pet. (done)
*/

int main ()
{
//baseClass derivedClass();
  Pet aPet("Peter");
  Cat aCat("Foo");
  Dog aDog("Bar");


  aPet.sleep();
  aCat.sleep();
  aDog.sleep();

//derivedClass.method();
  aPet.drink();

  // end program
  return 0;
}
