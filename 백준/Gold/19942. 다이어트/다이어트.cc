#include <iostream>
#include <vector>
#include <limits>
#include <bitset>
using namespace std;

int n;
int a, b, c, d;
int answer = numeric_limits<int>::max(); // 초기값 설정
vector<int> answer_combination; // 최적의 조합을 저장

void distinguish(int combi, const vector<vector<int>> &matrix) {
    vector<int> total_arr(5, 0);
    vector<int> current_combination;

    // 현재 조합에서 선택된 식재료를 확인
    for (int i = 0; i < n; i++) {
        if (combi & (1 << i)) {
            current_combination.push_back(i + 1); // 식재료 번호 저장
            for (int j = 0; j < 5; j++) {
                total_arr[j] += matrix[i][j];
            }
        }
    }

    // 최소 영양소 조건을 만족하는지 확인
    if (total_arr[0] >= a && total_arr[1] >= b && total_arr[2] >= c && total_arr[3] >= d) {
        if (answer > total_arr[4]) {
            // 더 낮은 비용 발견
            answer = total_arr[4];
            answer_combination = current_combination;
        } else if (answer == total_arr[4] && current_combination < answer_combination) {
            // 비용이 동일한 경우 사전순으로 더 빠른 조합 선택
            answer_combination = current_combination;
        }
    }
}

int main() {
    cin >> n;
    cin >> a >> b >> c >> d;

    vector<vector<int>> matrix(n, vector<int>(5, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> matrix[i][j];
        }
    }

    // 모든 조합 탐색
    for (int combi = 1; combi < (1 << n); combi++) {
        distinguish(combi, matrix);
    }

    // 결과 출력
    if (answer == numeric_limits<int>::max()) {
        cout << "-1" << endl;
    } else {
        cout << answer << endl;
        for (int i : answer_combination) {
            cout << i << " ";
        }
        cout << endl; // 출력 형식에 줄바꿈 추가
    }

    return 0;
}
