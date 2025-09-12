#include <iostream>
#include <string>
using namespace std;

int main()
{  
  int age = 96;
  bool canDrive;
  if(age>= 16)
  {
    canDrive = true;
  }
  else
  {
    canDrive = false;
  }
  
  cout << "I am " << age << " years old" << endl;
  if(canDrive)
  {
    cout<< "i am car" << endl;
  }
  else
  {
    cout<<"i am not car" << endl;
  }
  
  return 0;
}