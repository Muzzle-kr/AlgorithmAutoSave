#include <iostream>
#include <vector>

using namespace std;
int n;
int answer = -1004;

int main() {
    cin >> n;
    vector<int> dp;

    int sum = 0;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        sum += num;
        answer = max(answer, sum);
        if (sum < 0) sum = 0;
    }

    cout << answer << endl;
    return 0;
}