#include <iostream>
#include <vector>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> v = {a, b, c};

    int n;
    cin >> n;
    
    int answer = 0;

    for (int i = 0; i < n; i++) {
        int total = 0;

        for (int j = 0; j < 3; j++) {
            int a, b, c;
            cin >> a >> b >> c;
            
            total += v[0] * a;
            total += v[1] * b;
            total += v[2] * c;
        }

        answer = max(answer, total);
    }

    cout << answer << endl;
    
    return 0;
}