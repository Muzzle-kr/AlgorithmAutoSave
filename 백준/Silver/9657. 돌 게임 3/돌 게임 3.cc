#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    
    if (n % 7 == 0 || n % 7 == 2) { // 'or'를 '||'로 변경
        cout << "CY" << endl;
    } else {
        cout << "SK" << endl;
    }
}
