#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

void dfs(int node, vvi &tree, vi &visited) {
    visited[node] = 1;
    
    for (int next : tree[node]) {
        if (!visited[next]) {
            dfs(next, tree, visited);
        }
    }
    return;
}

int root = -1;

int main() {
   int n;
   cin >> n;

    vvi tree(n);

   for (int i = 0; i < n; i++) {
        int m;
        cin >> m;

       if (m == -1) {
            root = i;
        } else {
            tree[m].push_back(i);
        }
   }

    int remove_node;
    cin >> remove_node;

    vi visited(n, 0);
    if (remove_node == root) {
        cout << 0 << endl;
        return 0;
    } else {
        dfs(remove_node, tree, visited);
    }


    int result = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 1) continue;

        if (tree[i].empty()) {
            result++;
        } else {
            bool has_unvisited_child = false;
            for (int child : tree[i]) {
                if (!visited[child]) {
                    has_unvisited_child = true;
                    break;
                }
            }
            if (!has_unvisited_child) {
                result++;
            }
        }
    }
    cout << result << endl;
}