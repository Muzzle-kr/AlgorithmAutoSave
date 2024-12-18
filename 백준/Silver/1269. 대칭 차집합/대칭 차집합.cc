#include <iostream>
#include <set>
#include <algorithm>

using namespace std;
int n, m;

int main() {
    cin >> n >> m;

    set<int> s1;
    set<int> s2;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        s1.insert(x);
    }

    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        s2.insert(x);
    }

    set<int> set_diff1;
    set<int> set_diff2;

    set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(set_diff1, set_diff1.begin()));
    set_difference(s2.begin(), s2.end(), s1.begin(), s1.end(), inserter(set_diff2, set_diff2.begin()));

    cout << set_diff1.size() + set_diff2.size() << endl;
    return 0;
}