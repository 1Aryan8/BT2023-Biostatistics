#include <stdio.h>
int main() 
{
   long int num;
   //printf("enter the number");
   scanf("%ld",&num);
   long int den=2,  LPFactor=0;
   while(num != 0) 
   {
      if(num % den !=0) den = den + 1;
      else 
      {
        LPFactor = num;
        num = num / den;
        if(num == 1) 
        {
            printf("\n %ld is the largest prime factor !",LPFactor);
         
            break;
        }
         
      }
      printf("\n num=%ld den=%ld LPFactor=%ld \n",num,den,LPFactor);
   }
   return 0;
}
