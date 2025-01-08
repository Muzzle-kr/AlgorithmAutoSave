#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef map<string, vector<tuple<string, bool>>> graph;
typedef map<string, bool> msb;

bool is_all_visited(graph routes) {
    for (auto &r : routes) {
        for (auto &d : r.second) {
            if (!get<1>(d)) {
                return false;
            }
        }
    }

    return true;
}

bool dfs(string from, graph &routes, vs &answer, int ticket_count) {
    if (answer.size() == ticket_count + 1) {
        return true;
    }

    for (auto &dest : routes[from]) {
        if (get<1>(dest)) {
            continue;
        }

        get<1>(dest) = true;
        answer.push_back(get<0>(dest));
        
        if (dfs(get<0>(dest), routes, answer, ticket_count)) {
            return true;
        }

        get<1>(dest) = false;
        answer.pop_back();
    }

    return false;
}
vs solution(vvs tickets) {
    vs answer;
    graph routes;
    
    for (auto &ticket : tickets) {
        routes[ticket[0]].push_back({ticket[1], false});
    }

    for (auto &g : routes) {
        sort(g.second.begin(), g.second.end());
    }

    answer.push_back("ICN"); 
    dfs("ICN", routes, answer, tickets.size());
    return answer;
}
