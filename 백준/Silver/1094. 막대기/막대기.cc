// 1. 지민이가 가지고 있는 막대의 길이를 모두 더한다. 처음에는 64cm 막대 하나만 가지고 있다. 이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
// 1-1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
// 1-2. 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
// 1-3. 이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;
int answer = 1;
int x = 0;
int main() {
    cin >> x;

    vector<int> stick = {64};

    while (accumulate(stick.begin(), stick.end(), 0) != x) {
        int last_stick = stick.back();

        stick.pop_back();
        stick.push_back(last_stick / 2);

        if (accumulate(stick.begin(), stick.end(), 0) >= x) {
            continue;
        }

        if (accumulate(stick.begin(), stick.end(), 0) < x) {
            answer++;
            stick.push_back(last_stick / 2);
        }        
    }

    cout << answer << endl;
    return 0;
}