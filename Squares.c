/* https://projecteuler.net/problem=6

Sum square difference
Problem 6


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

*/

#include <stdio.h>

int squares (int n){        // (int n) it's the number that we will use to make the count. (100)

int d;                      // (int d) it's the difference 
int s=0;                    // (int s) it's the sum of the squares
int q=0;                    // (int q) it's the square of the sum

for (int i =1; i<=n; i++){  // Cicle for to find the sum of the quares (int s)
s=s+(i*i);
}

for(int j=1; j<=n; j++){    // Cicle for to find the sum...
	q=q+j;
}
q=q*q;                      //... and then make the square of the sum (int q)

d=q-s;                      // difference between the square of the sum (int q) and the sum of the squares (int s) 

return d;                   // return (int d)
}

void main () {
	int n;
	printf("Insert a number:");
	scanf("%d",&n);
	putchar('\n');

	printf("The difference between the square of the sum and the sum of the squares is: %d\n",squares(n));
} 
