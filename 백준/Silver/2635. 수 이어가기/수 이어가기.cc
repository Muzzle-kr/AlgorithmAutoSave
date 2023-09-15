#include <iostream>
#include <vector>

using namespace std;
int n;
int ans = 0;
vector<int> ans_arr;

void resolve() {

    for (int i = 1; i < n + 1; i++) {
        vector<int> arr;
        arr.push_back(n);
        arr.push_back(i);
        

        while (true) {  // 무한 루프로 변경
            int size = arr.size();
            if (size >= 2 && arr[size - 2] - arr[size - 1] >= 0) {
                arr.push_back(arr[size - 2] - arr[size - 1]);
            } else {
                break;
            }
        }

        if (ans < arr.size()) {
            ans = arr.size();
            ans_arr = arr;
        }
    }
    
    if (ans == 0) {
        return;
    } else {
        cout << ans << endl;

        for (int i = 0; i < ans_arr.size(); i++) {
            cout << ans_arr[i] << " ";
        }
        return;
    }
}
void input() {
    cin >> n;
}

int main() {
    input();
    resolve();  
}

