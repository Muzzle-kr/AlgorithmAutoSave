#include <iostream>
#include <array>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;


int main() {
    vector<int> A(10);
    vector<int> B(10);
    int total_a = 0;
    int total_b = 0;
    char last_winner = 'D';
    
    for (int i = 0; i < 10; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < 10; i++) {
        cin >> B[i];
    }

    for (int i = 0; i < 10; i++) {
        int a = A[i];
        int b = B[i];
        
        if (a > b) {
            total_a += 3;
            last_winner = 'A';
        } else if(a < b) {
            total_b += 3;
            last_winner = 'B';
        } else {
            total_a += 1;
            total_b += 1;
        }
    }
    
    cout << total_a << " " << total_b << endl;
    
    if (total_a > total_b) {
        cout << "A" << endl;
    } else if (total_a < total_b) {
        cout << "B" << endl;
    } else {
        cout << last_winner << endl;
    }
}