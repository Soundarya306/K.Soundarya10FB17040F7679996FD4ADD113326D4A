#include<stdio.h>

//Recursive function to calculate factorial of a number
unsigned long factorial(int n)
{
  //base case:if'n'is0or1
  if(n<1){
    return1;
}

// use the recurrence relation
return n*factorial(n-1);
}

int main()
{
  int n=5;
printf("The Factorial of%d is%1u",n,factorial(n));

return 0;

  
