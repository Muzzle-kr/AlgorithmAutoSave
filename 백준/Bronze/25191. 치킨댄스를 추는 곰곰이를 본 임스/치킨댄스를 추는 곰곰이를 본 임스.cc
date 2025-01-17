#include <iostream>
#include <vector>


using namespace std;

int main() {
    int chicken;
    cin >> chicken;

    int cola, beer;
    cin >> cola >> beer;

    cout << min(chicken, cola / 2 + beer) << endl;
    return 0;
}