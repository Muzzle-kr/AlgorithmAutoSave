#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int N, A;

bool enter_dungeon(long long max_hp, const vector<tuple<int, long long, long long>>& rooms_info) {
    long long current_hp = max_hp;
    long long current_atk = A;

    for (auto [t, atk, hp] : rooms_info) {
        if (t == 1) {
            long long attack_count = (hp + current_atk - 1) / current_atk;

            // 플레이어가 받는 피해량
            long long damage_taken = (attack_count - 1) * atk;

            if (current_hp <= damage_taken) {
                return false;
            }

            current_hp -= damage_taken;
        } else {
            current_atk += atk;
            current_hp = min(current_hp + hp, max_hp);
        }
    }
    return true;
}

int main() {
    cin >> N >> A;

    vector<tuple<int, long long, long long>> rooms_info;

    for (int i = 0; i < N; i++) {
        int t;
        long long a, h;
        cin >> t >> a >> h;
        rooms_info.push_back({t, a, h});
    }

    long long left = 1;  // 최소 HP는 1 이상
    long long right = 9e18;
    long long answer = right;

    while (left <= right) {
        long long max_hp = (left + right) / 2;

        if (enter_dungeon(max_hp, rooms_info)) {
            answer = min(answer, max_hp);
            right = max_hp - 1;
        } else {
            left = max_hp + 1;
        }
    }

    cout << answer << endl;
    return 0;
}
