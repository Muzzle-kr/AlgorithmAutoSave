#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

bool isDigit(const string& str) {
    return !str.empty() && all_of(str.begin(), str.end(), ::isdigit);
}

int main() {
    ios::sync_with_stdio(false); // 입출력 비동기화 비활성화
    cin.tie(nullptr);            // cout과 cin의 묶음 해제
    
    unordered_map<string, int> poketmonMapNameIndex;
    unordered_map<int, string> poketmonMapIndexName;
    int n, m;
    
    cin >> n >> m;

    // 포켓몬 이름과 번호를 맵에 저장
    for (int i = 1; i <= n; i++) {
        string name;
        cin >> name;
        poketmonMapNameIndex[name] = i;
        poketmonMapIndexName[i] = name;
    }
    
    // 질의 처리
    for (int i = 0; i < m; i++) {
        string question;
        cin >> question;
        
        if (isDigit(question)) {
            // 숫자일 경우 번호를 사용해 이름 출력
            cout << poketmonMapIndexName[stoi(question)] << "\n";
        } else {
            // 문자열일 경우 이름을 사용해 번호 출력
            auto it = poketmonMapNameIndex.find(question);
            if (it != poketmonMapNameIndex.end()) {
                cout << it->second << "\n";
            }
        }
    }
    return 0;
}
