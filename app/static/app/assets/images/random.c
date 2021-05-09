#include<stdio.h>

int main()
{
	printf("Hiii");
	for(int i=0; i<3; i++)
		fork();
}