//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution{
  public:	
	int distinctSubsequences(string s)
	{
	    // Your code goes here
	    
	    const int mod=1000000007;
	    
	    int n=s.length();
	    
	    int dp[n+1];
	    
	    dp[0]=1;    //for empty subseq
	   
	    vector<int> lastOccAt(26,-1);  //initialize last occurred position of all 26 lower case alphabets to -1
	    
	    for(int i=1;i<=n;i++){
	        
	        dp[i]=2*dp[i-1]%mod;
	        
	        if(lastOccAt[s[i-1]-'a']!=-1)   //check if current char occurred earlier
	            
	               dp[i]=(dp[i]-dp[lastOccAt[s[i-1]-'a']])%mod;  
	        
	        lastOccAt[s[i-1]-'a']=i-1; //update the last occurrence
	    }
	    
	    if(dp[n]<0)
	    
	        dp[n]+=mod;
	        
	    return dp[n];
	    
	}
};

//{ Driver Code Starts.

int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s;
   		cin >> s;

        Solution ob;
   		cout << ob.distinctSubsequences(s) << "\n";
   	}

    return 0;
}
// } Driver Code Ends