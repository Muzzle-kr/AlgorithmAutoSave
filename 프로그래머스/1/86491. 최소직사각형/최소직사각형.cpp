#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef vector<vector<int>> vvi;
int answer = 1e9;

int solution(vector<vector<int>> sizes) {
    int width = 0, height = 0;
    
    for (int i = 0; i < sizes.size(); i++) {
        if (sizes[i][0] > sizes[i][1]) {
            width = max(width, sizes[i][0]);
            height = max(height, sizes[i][1]);
        } else {
            width = max(width, sizes[i][1]);
            height = max(height, sizes[i][0]);
        }
    }
    return width * height;
}