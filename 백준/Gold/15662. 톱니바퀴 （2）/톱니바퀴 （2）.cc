#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> sawtooths;

void clockwise_shift(string& sawtooth) {
    char tmp = sawtooth[7];
    sawtooth = tmp + sawtooth.substr(0, 7);
}

void counter_clockwise_shift(string& sawtooth) {
    char tmp = sawtooth[0];
    sawtooth = sawtooth.substr(1) + tmp;
}

void propagate(int index, int dir, vector<int>& rotate_dir) {
    // 이미 확인된 톱니라면 건너뛰기
    if (rotate_dir[index] != 0) {
        return;
    }

    // 현재 톱니 회전 방향 설정
    rotate_dir[index] = dir;

    // 왼쪽 전파
    if (index > 0 && rotate_dir[index - 1] == 0) {
        if (sawtooths[index][6] != sawtooths[index - 1][2]) {
            propagate(index - 1, -dir, rotate_dir);
        }
    }

    // 오른쪽 전파
    if (index < sawtooths.size() - 1 && rotate_dir[index + 1] == 0) {
        if (sawtooths[index][2] != sawtooths[index + 1][6]) {
            propagate(index + 1, -dir, rotate_dir);
        }
    }
}

int main() {
    int n, t;
    cin >> n;

    // 톱니 입력받기
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        sawtooths.push_back(s);
    }

    cin >> t;

    for (int i = 0; i < t; i++) {
        int num, dir;
        cin >> num >> dir;
        num -= 1;  // 인덱스 보정 (1-based → 0-based)

        // 각 톱니의 회전 방향을 저장할 벡터
        vector<int> rotate_dir(n, 0);

        // 회전 전파 설정
        propagate(num, dir, rotate_dir);

        // 회전 방향에 따라 톱니 회전
        for (int j = 0; j < n; j++) {
            if (rotate_dir[j] == 1) {
                clockwise_shift(sawtooths[j]);
            } else if (rotate_dir[j] == -1) {
                counter_clockwise_shift(sawtooths[j]);
            }
        }
    }

    // 12시 방향이 '1'인 톱니 개수 계산
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (sawtooths[i][0] == '1') {
            answer++;
        }
    }

    cout << answer << endl;
    return 0;
}
