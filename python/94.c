#include<stdio.h>
int main()
{
    int arr[100],n,m,i;
    scanf("%d%d",&n,&m);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("%d",arr[m-1]);
}
