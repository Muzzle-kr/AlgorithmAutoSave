#include <bits/stdc++.h>

using namespace std;

int is_prime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    for (int i = 3; i * i <= n; i+= 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}


int solution(string numbers) {
    int answer = 0;
    set<int> primes;
    vector<char> digits(numbers.begin(), numbers.end());
    sort(digits.begin(), digits.end());
     
    do {
        for (int i = 1; i <= digits.size(); i++) {
            string s = string(digits.begin(), digits.begin() + i);
            int number = stoi(s);
            if (is_prime(number)) {
                primes.insert(number);
            }
        }
    } while (next_permutation(digits.begin(), digits.end()));
    
    
    return primes.size();
}