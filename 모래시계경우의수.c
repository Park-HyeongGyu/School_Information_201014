#include <stdio.h>
#include <stdlib.h>

int MakeNumberPositive(int num);
int GetGCD(int A, int B); //GCD = the greatest commom denominator

int main()
{
	int A, B;
	printf("Input A:");
	scanf("%d",&A);
	printf("Input B:");
	scanf("%d",&B);
	int gcd = GetGCD(A, B);
	

	if(gcd!=1)
	{
		printf("두 수가 서로소가 아니므로 모든 시간을 측정할 수 없습니다.\n");
		//printf("최대공약수:%d", gcd);
		return 0;
	}
	
	//|mA + nB| = result
	int *array_m = malloc(sizeof(int) * A);
	int *array_n = malloc(sizeof(int) * A);
	
	for(int i=0 ; i<A; i++) array_m[i]=0;
	for(int i=0 ; i<A; i++) array_n[i]=0;
	
	for(int m=0 ; m<=B ; m++)
	{
		for(int n=0; n<=A ; n++)
		{
			int result = MakeNumberPositive(m*A - n*B);
			for(int check=0 ; check<A ; check++)
			{
				if(result==check+1 && array_m[check]==0 && array_n[check]==0)
				{
					array_m[check]=m;
					array_n[check]=n;
				}
			}
		}
	}
	
	for(int c=0 ; c<A ; c++)
	{
		printf("|%dX%d - %dX%d| = %d\n", array_m[c], A, array_n[c], B, c+1);
	}

	
	free(array_m);
	free(array_n);
	return 0;
}

int MakeNumberPositive(int num)
{
	if(num>=0) return num;
	else return num*(-1);
}

int GetGCD(int a, int b)
{
	//유클리드 호제법 
	int c;
	while(b!=0)
	{
		c = a%b;
		a=b;
		b=c;
	}
	return a;
}
