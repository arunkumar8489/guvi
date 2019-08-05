#include<stdio.h>
int main()
{
    int n,m,s=0,v;
    scanf("%d",&n);
    for(m=1;m<=n;m++)
    {
        scanf("%d",&v);
        s+=v;
        
    }
    printf("%d",s);
    
}
