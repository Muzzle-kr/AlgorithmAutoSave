#include <iostream>

using namespace std;


int main() {
    while (true) {
        int m;
        cin >> m;

        if (cin.eof()) break; 

        int remainder = 0;
        for (int j = 1; ; j++) {
            remainder = (remainder * 10 + 1) % m;
            if (remainder == 0) {
                cout << j << endl;
                break;
            }
        }
    }
    return 0;

}
