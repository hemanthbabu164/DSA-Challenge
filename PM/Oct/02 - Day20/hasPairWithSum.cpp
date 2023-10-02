//Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

//For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool hasPairWithSum(vector<int> nums, int k) {
    unordered_set<int> seen; // unordered set to store seen numbers

    for (int num : nums) {

        int complement = k - num; // complement needed to reach k

        // If the complement is in the set, we found a pair that adds up to k
        if (seen.find(complement) != seen.end()) {
            return true;
        }

        seen.insert(num); // Add the current number to the set
    }

    // No pair was found
    return false;
}

int main() {

    vector<int> nums = {10, 15, 3, 8};
    int k = 18;

    if (hasPairWithSum(nums, k)) {
        cout << "True, there exists a pair that adds up to " << k << endl;
    } else {
        cout << "False, there is no pair that adds up to " << k << endl;
    }

    return 0;
}

