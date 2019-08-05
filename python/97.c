#include <stdio.h>
int main()
{
    int n,c=0;
    scanf("%d",&n);
    while(n!=0)
    {
        c*=10;
        c=c+n%10;
        n/=10;
    }
    printf("%d",c);
}
