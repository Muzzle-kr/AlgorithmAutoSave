#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>

using namespace std;
int n, first, last = 0; 
long long answer = 0;

vector<tuple<int, int>> arr;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        arr.push_back(make_tuple(a, b));
    }

    sort(arr.begin(), arr.end());

    first = get<0>(arr[0]);
    last = get<1>(arr[0]);
    answer = last - first;

    for (int i = 1; i < n; i++) {
        int s = get<0>(arr[i]);
        int e = get<1>(arr[i]);

        if (e <= last) {
            continue;
        } else if(e > last && s <= last) {
            answer += e - last;
            last = e;
        } else if(e > last && s > last) {
            answer += e - s;
            last = e;
            first = s;
        }
    }

    cout << answer << endl;
    return 0;
}

