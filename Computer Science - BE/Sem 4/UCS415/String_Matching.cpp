#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vvi vector<vi>
#define vc vector<char>
#define vvc vector<vc>
#define pb push_back
#define pf push_front
#define test  \
    ll t;     \
    cin >> t; \
    while (t--)
#define mod 1000000007
#define fo ios_base::sync_with_stdio(false);
#define fi cin.tie(NULL);
vector<int> search(string str, string pat)
{
    int n = str.size();
    int m = pat.size();
    vector<int> v;
    for (int i = 0; i <= n - m; i++)
    {
        int k = 0;
        int index = i + m;
        for (int j = i; j < index; j++)
        {
            if (str[j] == pat[k])
            {
                k++;
                continue;
            }
            else
            {
                break;
            }
        }
        if (k == m)
        {
            v.push_back(i);
        }
    }
    return v;
}
int main()
{
    string str = "abccccbc";
    string p = "bc";
    vector<int> a;
    a = search(str, p);
    for (auto it : a)
    {
        cout << it;
    }
    return 0;
}
