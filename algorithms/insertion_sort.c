//insertion sort
// faster for small amount of entries
#include<stdio.h>
void main()
{
int n,i,j,k;
printf("number of entries : ");
scanf("%d",&n);//let n=3
int a[n];//create an array of size n
//taking inputs
printf("Enter values : \n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);// let a={3,2,1}
//sorting begins
//like sorting a pack of cards
for(i=1;i<n;i++)
{
k=a[i];
j=i-1;
while(j>=0 && a[j]>k)
{
a[j+1]=a[j];
j--;
}
a[j+1]=k;
}
//getting sorted output
printf("Sorted : \n");
for(i=0;i<n;i++)
printf("%d,",a[i]);
printf("\n");
}
