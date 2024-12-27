#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int n;
int hp;
vector<int> h;
vector<int> p;
int answer = 0;

void thank_you(int idx, int remain_hp, int pleasure) {
    if (idx == n) {
        if (remain_hp > 0) {
            answer = max(answer, pleasure);
        }
        return;
    }

    thank_you(idx + 1, remain_hp - h[idx], pleasure + p[idx]);
    thank_you(idx + 1, remain_hp, pleasure);
}

int main() {
    cin >> n;
    cin.ignore();

    string h_s, p_s;
    getline(cin, h_s);
    getline(cin, p_s);

    stringstream h_ss(h_s);
    stringstream p_ss(p_s);


    int temp;

    while (h_ss >> temp) {
        h.push_back(temp);
    }

    while (p_ss >> temp) {
        p.push_back(temp);
    }


    thank_you(0, 100, 0);

    cout << answer << endl;
    return 0;
}