// guess the number.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    //seed rng
    srand(time(0));
    int max = 2000000000000000001;
    int num = rand() % max;
    int numGus = -1;

    while (numGus != num)
    {
        //cout << num << endl;
        cout << "guess the number dumbo its 0-" << max << endl;
        cin >> numGus;
        cout << numGus << endl;

        if (numGus > num)
        {
            cout << " too high dumbo" << endl;
        }
        else if (numGus < num)
        {
            cout << "too low dumbo" << endl;
        }
        else
        {
            cout << "nice job dumbo you donkey stupid fat and ugly" << endl;
        }
        //cout << "your wrong dumbo" << endl;
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
