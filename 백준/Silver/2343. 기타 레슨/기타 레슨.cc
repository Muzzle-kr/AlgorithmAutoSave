#include <iostream>
#include <vector>

int n, m;

using namespace std;

int main() {
    cin >> n >> m;
    int left = 0;
    int right = 1e9;
    vector<int> a;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        left = max(left, x);   
        a.push_back(x);
    }

    int answer = 0;
    while (left <= right) {
        int mid = (left + right) / 2;

        long long sum = 0;
        int cnt = 0;

        int index = 0;
        
        while (index < n) {
            if (sum + a[index] <= mid) {
                sum += a[index];
            } else {
                cnt++;
                sum = a[index];
            }        
            index++;
        }
        
        if (a[index - 1] > 0) {
            cnt++;
        }

        if (cnt <= m) {
            right = mid - 1;
            answer = mid;
        } else {
            left = mid + 1;
        }
    }
    
    cout << answer << endl;
    return 0;
}

