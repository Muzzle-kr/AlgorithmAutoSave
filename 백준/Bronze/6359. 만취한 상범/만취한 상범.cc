#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> v(104, 0);
vector<int> answer(104, 0);
int main() {
    for (int i = 1; i <= 100; i++) {
        for (int j = i; j <= 100 + i; j+=i) {
            if (j > 100) {
                break;
            }
            
            v[j] = abs(v[j] - 1);
        }
        
        int total = 0;
        
        for (int j = 1; j <= i; j++) {
            if (v[j] == 1) {
                total++;
            }
        }

        answer[i] = total;
    }

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        cout << answer[x] << endl;
    }
    
    return 0;
}