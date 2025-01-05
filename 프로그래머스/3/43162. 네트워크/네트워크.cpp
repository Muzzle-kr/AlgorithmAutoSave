#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef vector<vector<int>> vvi;

void dfs(int start, int n, vvi & computers, vector<int> & visited) {
    visited[start] = 1;
    
    for (int end = 0; end < n; end++) { 
        if (start == end) continue;
        
        if (computers[start][end] == 1 && !visited[end]) {
            dfs(end, n, computers, visited);
        }
    }    
} 
    
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> visited(n + 1, 0);
    
    for (int start = 0; start < n; start++) {
        if (!visited[start]) {
            answer++;
            dfs(start, n, computers, visited);
        }
    }
    
    return answer;
}