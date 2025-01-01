#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (vector<int> command : commands) {
        int a = command[0];
        int b = command[1];
        int k = command[2];
        vector<int> new_array;

        for (int i = a - 1; i < b; i++) {
            new_array.push_back(array[i]);
        }

        sort(new_array.begin(), new_array.end());
        answer.push_back(new_array[k-1]);
    }
    return answer;
}