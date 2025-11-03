#include <iostream>
using namespace std;

int main()
{
    int n = 4;
    char charru = 'A';
    // int vallu = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << charru;
            charru += 1;
        }
        cout << endl;
    }
}