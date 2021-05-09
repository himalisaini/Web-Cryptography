#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int max_index = 7;
int lb=0 , ub=4;

void disp_array(int a[])
{
  for(int i=0;i<=ub;i++)
  {
    printf("%d ",a[i]);
  }
  printf("\nLB = %d  UB = %d  Max = %d\n",lb,ub,max_index);

}

void insert(int a[])
{
  int ind,val;
  printf("\nEnter the index where the element has to be inserted :");
  scanf("%d",&ind);

  printf("\nEnter the int value to be inserted :");
  scanf("%d",&val);

  if (ub == max_index)
  {
    printf("\nOverflow.");
    exit(0);
  } 
  for(int k=ub; k>=ind; k--)
  {
    a[k+1] = a[k];
  }
  a[ind] = val;
  if(ind>ub)
  {
    ub = ind;
  }
  else{
    ub++;
  }

  disp_array(a);

}

void del(int a[])
{
  int ind,val;
  printf("\nEnter the index of the element to be deleted :");
  scanf("%d",&ind);

  if (ub <0)
  {
    printf("\nUnderflow.");
    exit(0);
  } 
  for(int k=ind; k<=ub; k++)
  {
    a[k] = a[k+1];
  }
  ub--;
  disp_array(a);
}

void min_max(int a[])
{
  int min , max;
  min = max = a[0];
  for(int i=lb+1;i<=ub;i++)
  {
    if(a[i]<min)
    {
      min = a[i];
    }
    if(a[i]>max)
    {
      max = a[i];
    }

  }

  printf("\nMax : %d  Min : %d\n",max,min);
}

int main() {
  int a[8]={1,2,3,4,5};
  int ch;
  disp_array(a);
  while(ch!=4){
  printf("Select an option :\n1.Insert element\n2.Delete element\n3.Find max/min\n4.exit\n");
  scanf("%d",&ch);
  switch (ch)
  {
    case 1: insert(a);
    break;

    case 2: del(a);
    break;

    case 3: min_max(a);
    break;

    case 4: exit(0);
    break;

    default: printf("\nWrong choice..try again.");
  }
  }
  return 0;
  
}