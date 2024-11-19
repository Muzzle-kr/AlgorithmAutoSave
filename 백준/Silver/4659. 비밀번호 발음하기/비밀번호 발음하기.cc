#include <iostream>
#include <vector>

using namespace std;
vector<char> vowel = {'a', 'e', 'i', 'o', 'u'};

bool dfs(string word, int index, int vowel_count, int consonant_count, int same_count, bool include_vowel) {
    if (index == word.size()) {
        return include_vowel && vowel_count < 3 && consonant_count < 3 && same_count < 2;
    }

    if (vowel_count == 3 || consonant_count == 3 || same_count == 2) {
        return false;
    }

    char w = word[index];
    bool is_vowel = find(vowel.begin(), vowel.end(), w) != vowel.end();

    int new_vowel_count = is_vowel ? vowel_count + 1 : 0;
    int new_consonant_count = is_vowel ? 0 : consonant_count + 1;
    int new_same_count = (index > 0 && w == word[index - 1] && w != 'e' && w != 'o') ? same_count + 1 : 1;
    bool new_include_vowel = include_vowel || is_vowel;

    return dfs(word, index + 1, new_vowel_count, new_consonant_count, new_same_count, new_include_vowel);
}


int main() {
    while (true) {
        string word;
        cin >> word;

        if (word == "end") {
            break;
        }

        bool result = dfs(word, 0, 0, 0, 0, false);

        if (result) {
            cout << "<" << word << "> is acceptable." << endl;
        } else {
            cout << "<" << word << "> is not acceptable." << endl;
        }
    }

    return 0;

}
