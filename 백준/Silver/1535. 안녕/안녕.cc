#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int n;
int hp;
vector<int> h;
vector<int> p;
int answer = 0;
vector<int> dp(100, 0);

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        h.push_back(tmp);
    }

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        p.push_back(tmp);
    }

   for (int i = 0; i < n; i++) {
       for (int j = 99; j >= h[i]; j--) {
           dp[j] = max(dp[j], dp[j - h[i]] + p[i]);
       }
   }

    for (int i = 1; i < 100; i++) {
        answer = max(answer, dp[i]);
    }
    cout << answer << endl;
    return 0;
}