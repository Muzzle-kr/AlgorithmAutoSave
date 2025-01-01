#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comparsion(string a, string b) {
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> new_array;

    for (int i = 0; i < numbers.size(); i++) {
        new_array.push_back(to_string(numbers[i]));
    }

    sort(new_array.begin(), new_array.end(), comparsion);

    for (string s : new_array) {
        answer += s;
    }

    if (answer[0] == '0') {
        return "0";
    }

    return answer;
}