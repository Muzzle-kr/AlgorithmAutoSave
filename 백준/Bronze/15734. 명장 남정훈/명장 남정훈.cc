#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    while (c >= 1) {
        if (a > b) {
            b++;
            c--;
        } else if(a < b) {
            a++;
            c--;
        } else {
            if (c >= 2) {
                a++;
                b++;
                c -= 2;
            } else if (c == 1) {
                break;
            }
        }
        
    }

    cout << min(a, b) * 2 << endl;


    return 0;
}
