#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define test  \
    ll t;     \
    cin >> t; \
    while (t--)
#define mod 1000000007
#define fo ios_base::sync_with_stdio(false);
#define fi cin.tie(NULL);
int binarySearch(int A[], int l, int r, int x)
{
    while (l <= r)
    {
        int m = l + (r - l) / 2;
        if (A[m] == x)
            return m;
        if (A[m] < x)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}

int main()
{
    // fo;fi;
    cout << "number of elements :";
    int n;
    cin >> n;
    int a[n];
    cout << "enter the elements :";
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int x;
    cout << "Enter the element to find" << endl;
    cin >> x;
    int size = sizeof(a) / sizeof(a[0]);
    int ans = binarySearch(a, 0, size - 1, x);
    cout << "index of the element in the array ";
    cout << ans << endl;
    return 0;
}