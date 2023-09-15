#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> numli(n);
    for (int i = 0; i < n; i++) {
        cin >> numli[i];
    }
    
    sort(numli.begin(), numli.end());
    
    long long sum = 0;
    for (int i = 1; i <= k; i++) {
        sum += numli[n - i] - i + 1;
    }
    
    cout << sum << endl;
    
    return 0;
}