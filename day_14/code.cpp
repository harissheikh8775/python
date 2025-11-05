#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int binNum = 0;
    int decNum = 10;

    while (decNum > 0)
    {
        int a = decNum % 2;
        decNum = decNum / 2;
        binNum = binNum * 10 + a;
    }

    cout << binNum;
}