#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int w;
    int h;
    int n;
    cin >> w >> h;
    cin >> n;
    
    vector<int> cut_w;
    vector<int> cut_h;
    
    cut_w.push_back(0);
    cut_w.push_back(w);   
    
    cut_h.push_back(0);
    cut_h.push_back(h);
    
    for (int i = 0; i < n; i++) {
        int cr, num;
        cin >> cr >> num;
        
        if (cr == 0) {
            cut_h.push_back(num);    
        } else {
            cut_w.push_back(num);
        }
    }
    
    sort(cut_w.begin(), cut_w.end());
    sort(cut_h.begin(), cut_h.end());

    int max_w = 0;
    int max_h = 0;
    
    for (int i = 1; i < cut_w.size(); i++) {
        max_w = max(max_w, cut_w[i] - cut_w[i-1]);
    }

    for (int i = 1; i < cut_h.size(); i++) {
        max_h = max(max_h, cut_h[i] - cut_h[i-1]);
    }

    cout << max_w * max_h << endl;
    return 0;
}
