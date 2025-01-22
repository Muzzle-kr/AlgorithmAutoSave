#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v;
    vector<int> v2;

    for (int i = 0; i < 9; i++) {
        int x;
        cin >> x;
        v.push_back(x);
    }

    for (int i = 0; i < 9; i++) {
        int x;
        cin >> x;
        v2.push_back(x);
    }


    int total1 = 0;
    int total2 = 0;

    bool winning = false;

    
    for (int i = 0; i < 9; i++) {
        total1 += v[i];

        if (total1 > total2) {
            winning = true;
        }
        total2 += v2[i];

        
    }

    if (winning) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}