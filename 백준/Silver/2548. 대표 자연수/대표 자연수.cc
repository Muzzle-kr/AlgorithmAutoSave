#include <iostream>
#include <array>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    int m;
    cin >> m;
    
    vector<int> sorted_arr(m);
    
    for (int i = 0; i < m; i++) {
        cin >> sorted_arr[i];
    }
    
    sort(sorted_arr.begin(), sorted_arr.end());

    int minimum_total = 2000000000;
    int answer = 0;

    int mid_num = sorted_arr[m/2];
    
    for (int n = mid_num; n >= 0; n--) {
        int total = 0;
        
        for (int i=0; i < m; i++) {
            int abs_num = abs(sorted_arr[i] - n);
            total += abs_num;
        }

        if (total <= minimum_total) {
            minimum_total = total;
            answer = n;
        }
    }
    cout << answer << endl;
}