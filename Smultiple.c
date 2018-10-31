/*  https://projecteuler.net/problem=5

Smallest multiple
Problem 5



2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

*/

#include <stdio.h>

int smultiple (int n){  // (int n) is  kind of the limit number. (from 1 to n)

int s=1;                // (int s) is the smallest number
int k=n;                // (int k) is kind of a keeper number. Saves the original value of (int n)

	while(n>0){         // While (int n) it's bigger then zero   
		if(s%n==0){     // If the remainer of the actual smallest number(int s) for (int n) it's equal to zero...
		   n=n-1;       // ... let's decrement n, and return to the cicle while
		}
		else {          
			s= s+1;     // or else, increment s and...
			n=k;        // replace the original value of n
		}
	}
return s;               //return the smallest positive number that is evenly divisible by all of number from 1 to (int n)
}

void main () {

int i;

	printf("Define a limit: ");
	scanf("%d",&i);

	printf("\nThe smallest positive number that is evenly divisible by all\nof the numbers from 1 to 20 is: %d\n", smultiple(i));
}