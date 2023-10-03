/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.
*/


//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution{
    public:
    string colName (long long int n)
    {
            // your code here
        string result = "";
    
        while (n > 0) {
            int remainder = (n - 1) % 26; 
            result = char('A' + remainder) + result; 
            n = (n - 1) / 26; 
        }
        return result;
    }
};

//{ Driver Code Starts.
int main()
{
    int t; cin >> t;
    while (t--)
	{
		long long int n; cin >> n;
		Solution ob;
		cout << ob.colName (n) << '\n';
	}
}

// } Driver Code Ends