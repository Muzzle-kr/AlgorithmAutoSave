#include <iostream>
#include <vector>
#include <string>

using namespace std;
int n;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    cin.ignore();
    vector<int> arr(21);

    for (int i = 0; i < n; i++) {
        string order;
        getline(cin, order);
        

        if (order == "all") {
            for (int j = 1; j <= 20; j++) {
                arr[j] = 1;
            }
        } else if (order == "empty") {
            arr = vector<int>(21, 0);
        } else {
            auto it = order.find(" ");
            string cmd = order.substr(0, it);
            int num = stoi(order.substr(it + 1));

            if (cmd == "add") {
                arr[num] = 1;
            } else if (cmd == "remove") {
                arr[num] = 0;
            } else if (cmd == "check") {
                cout << arr[num] << '\n';
            } else if (cmd == "toggle") {
                arr[num] = !arr[num];
            }
        }
    }
    return 0;
}