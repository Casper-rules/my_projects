#include<iostream>
using namespace std;
int search(int arr[],int n,int l,int u)
{
if(l==u)
return u;
else
{
int middle=(l+u)/2;
if(n>arr[middle])
return(search(arr,n,middle+1,u));
else
return(search(arr,n,l,middle));
}
}

int main()
{
int n,arr[100];
int s;
cout<<"Enter the number of entries to be made : ";
cin>>n;
for(int i=0;i<n;i++)
{
cout<<"Enter element "<<i+1<<" in the array in sorted order : ";
cin>>arr[i]; 
}
cout<<"Enter the element to be searched : ";
cin>>s;
cout<<"index of the required number in the array is : "<<search(arr,s,0,n)<<endl;
}
