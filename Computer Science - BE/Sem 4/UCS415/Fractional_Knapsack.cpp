#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define test ll t;cin>>t;while(t--)
#define mod 1000000007
#define fo ios_base::sync_with_stdio(false);
#define fi cin.tie(NULL);
struct item{
    int value;
    int weight;
};
bool compare(item a,item b){
    double r1=double((a.value)/a.weight);
    double r2=double((b.value)/b.weight);
    return r1>r2;
}
double solve(item A[], int total_capacity, int n){
    sort(A,A+n,compare);
    int i=0;
    int current_weight=0;
    double final_value=0;
    for (int i=0;i<n;i++){
        if (current_weight+A[i].weight<=total_capacity){
            current_weight+=A[i].weight;
            final_value+=A[i].value;
        }
        else{
            int remain=total_capacity-current_weight;
            final_value+=A[i].value*(double(remain)/A[i].weight);
        }
    }
    return final_value;
}
int main(){
    // fo;fi;
    cout<<"Enter the number of testcases: ";
    test{
        int n,total_capacity;
        cout<<"Enter number of items: ";
        cin>>n;
        cout<<"Enter total capacity: ";
        cin>>total_capacity;
        item A[n];
        cout<<"Enter value and weight of each item: "<<endl;
        for (int i=0;i<n;i++){
            cin>>A[i].value>>A[i].weight;
        }
        cout<<"Maximum value can be obtained is: "<<solve(A,total_capacity,n)<<endl;
    }
    return 0;
}