#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> findAnagrams(const string &s, const string &w)
{
    vector<int> result;

    if (s.empty() || w.empty() || w.length() > s.length())
    {
        return result;
    }

    unordered_map<char, int> targetFreqMap;
    for (char c : w)
    {
        targetFreqMap[c]++;
    }

    unordered_map<char, int> currentWindowFreqMap;
    int windowSize = w.length();

    for (int i = 0; i < windowSize; ++i)
    {
        currentWindowFreqMap[s[i]]++;
    }

    if (currentWindowFreqMap == targetFreqMap)
    {
        result.push_back(0);
    }

    for (int i = windowSize; i < s.length(); ++i)
    {
        char removedChar = s[i - windowSize];
        char addedChar = s[i];

        currentWindowFreqMap[removedChar]--;
        if (currentWindowFreqMap[removedChar] == 0)
        {
            currentWindowFreqMap.erase(removedChar);
        }

        currentWindowFreqMap[addedChar]++;

        if (currentWindowFreqMap == targetFreqMap)
        {
            result.push_back(i - windowSize + 1);
        }
    }

    return result;
}

int main()
{
    string s = "abxaba";
    string w = "ab";
    vector<int> indices = findAnagrams(s, w);

    cout << "Anagram starting indices:";
    for (int index : indices)
    {
        cout << " " << index;
    }
    cout << endl;

    return 0;
}
