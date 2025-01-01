#include <string>
#include <vector>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    vector<int> quotation(10001, 0);
    
    for (int c : citations) {
        for (int i = 0; i <= c; i++) {
            quotation[i] += 1;
        }
    }
    
    for (int i = 0; i < 10001; i++) {
        if (quotation[i] < i) break;
        answer = i;
    }
    
    return answer;
}