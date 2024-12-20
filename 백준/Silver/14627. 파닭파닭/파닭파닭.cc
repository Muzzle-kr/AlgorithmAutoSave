#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n, m;
    cin >> n >> m;
    long long left = 0, right = 0;
    long long answer = 0;

    vector<long long> green_onions;

    for (long long i = 0; i < n; i++) {
        long long go;
        cin >> go;

        right = max(right, go);
        green_onions.push_back(go);
    }

    while (left <= right) {
        long long mid = (left + right) / 2;

        if (mid == 0) {
            break;
        }
        
        long long padak = 0;        
        long long jjatoori = 0;

        for (long long go : green_onions) {
            while (go >= mid && padak < m) {
                padak++;
                go -= mid;
            }
            jjatoori += go;
        }   

        if (padak >= m) {
            left = mid + 1;
            answer = jjatoori;
        } else {
            right = mid - 1;
        }
    }

    cout << answer << endl;
    return 0;
    
}