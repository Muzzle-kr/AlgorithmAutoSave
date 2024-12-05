#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

string a, b;

int main() {
   cin >> a >> b;

   size_t a_size = a.size();
   size_t b_size = b.size();

   int a_count = 0;
   int b_count = 0;

   string answer = "";

   int additional = 0;

   while (a_count < a_size || b_count < b_size || additional) {
       int a_num = (a_count < a_size) ? a[a_size - a_count - 1] - '0' : 0;
       int b_num = (b_count < b_size) ? b[b_size - b_count - 1] - '0' : 0;

       int total = a_num + b_num + additional;

       answer += to_string(total % 10);
       additional = total / 10;

       b_count++;
       a_count++;
   }

    reverse(answer.begin(), answer.end());
    cout << answer << endl;
    return 0;
}
